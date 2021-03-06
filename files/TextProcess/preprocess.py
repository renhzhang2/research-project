import os
import re
from PorterStemmer import PorterStemmer
import ipdb

def extract(l, pat, str, sub):
    l.extend(re.findall(pat,str))
    str = re.sub(pat, sub, str)
    return str

def tokenizeText(str):
    l = []
    # extract floating numbers -xxx.xxx
    pat = '[+-]?\d+\.\d+'
    str = extract(l, pat, str, '')

    #extract integer
    pat = '[\+\-]?\d+'
    str = extract(l, pat, str, '')

    # deal with U.S.A..
    str = re.sub('\.{2}', '.', str)

    #tokenization of '.'
    pat = '(?:\w+\.)+'
    str = extract(l, pat, str, '')

    #ipdb.set_trace()
    #tokenization of 's, 're, 'm
    pat = '\'s'
    str = re.sub(pat, '', str)

    pat = '\'re'
    str = re.sub(pat, ' are', str)

    pat = '\'m'
    str = re.sub(pat, ' am', str)

    # tokenization of dates: 01/01/2014, 01.01.2014, 01-01-2014, 01 01 2014,
    pat = '(\d{2}/\d{2}/\d{4}) | (\d{2}.\d{2}.\d{4}) | (\d{2}-\d{2}-\d{4}) | (\d{2}\s\d{2}\s\d{4})  '
    str = extract(l, pat, str, '')

    # tokenization of '-'
    pat = '(?:\w+-)+\w+'
    str = extract(l, pat, str, '')


    # remove special char: ,  .  "  :  ;  '  ? ( ) / -
    str = re.sub(',|\.|"|:|;|\'|\?|\(|\)', ' ', str)

    # extract normal words
    l.extend(re.split('\s+', str))

    l = filter(None, l)      #remove empty string
    return l
    #
def word_freq(s):
    '''
    :param s: a string
    :return:  a dictionary, key being a word that showing up in s, value being its counts
    '''
    return Counter(s.split())


def rm_space(s):
    return ' '.join(s.split())

def stem_words(l):
    ps = PorterStemmer()
    return [ps.stem(x, 0, len(x) - 1) for x in l]

def rm_stopwords(s):
    path = os.path.dirname(os.path.abspath(__file__)) + '/stopwords.txt'  
    with open(path, 'r') as f:
        sw = f.readlines()
    sw = [re.sub('[\n\s]', '', x) for x in sw]
    return ' '.join([w for w in s.split() if w.lower() not in sw])

def rm_special_char(s):
     
    special_char = [(u"\u2018", "'"), (u"\u2019", "'"), (u'\u201c', '"'),
                    (u'\u201d', '"'), (u"\u2014", '-'), (u'\u02bb', "'")]
    for u, v in special_char:
        s = s.replace(u, v)
    return s


def preprocess(s):

    s = rm_special_char(s)
    s = rm_space(s)
    s = rm_stopwords(s)
    l = tokenizeText(s)
    word_count_dict = {}
    for word in l:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
    return word_count_dict

