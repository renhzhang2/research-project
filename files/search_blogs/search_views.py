from django.shortcuts import render, render_to_response
#from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from Blogger_Retriever import get
from TextVisualize import visualize
from DB_Handling import BlogsDB
import ipdb
def search_blog_by_link(request):
    
    #return render(request, 'search_page.html')
    if 'link' not in request.GET:
        return HttpResponse('Please input an valid url to the blog')

    blog_link = request.GET['link']
    profile, blog, posts = get.get_blog_by_link(blog_link)

    # update the database
    dbh = BlogsDB.BlogsDB_Handler()
    dbh.batch_update(profile, blog, posts)

    if blog is None:
        return HttpResponse('Please input a valid url')

    wvt_uri = visualize.words_vs_time(posts)
    wc_uri = visualize.word_cloud(posts)
    ctx = Context({'posts': posts, 'blog_name': blog['name'].replace("\'", ''), 'wf_vs_time': wvt_uri, 'word_cloud':wc_uri})
    return render(request, 'blog_search_result.html', ctx)
    #return render_to_response('blog_search_result.html', {'posts': posts, 'blog_name': blog['name']},
