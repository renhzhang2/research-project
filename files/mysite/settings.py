"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
#import django
#from django.contrib import staticfiles
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mlo3g8e4g+q(nbh%h2=g#7p&d!3ql%eswl#*#_v#kyl+=wofe_'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = [
'.nlp.eecs.umich.edu',
'.nlp.eecs.umich.edu.'
]

DEBUG = True
# Application definition

INSTALLED_APPS = (

    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    'Blogger_Retriever',
    'search_blogs',
    'django.contrib.staticfiles',
)

# ADMINS
ADMINS = (
    ('Renhan Zhang', 'renhzhang2@gmail.com'),
)
MIDDLEWARE_CLASSES = (

    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',

)
SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (
    ( 'Renhan Zhang', 'renhzhang2@gmail.com'),
)

ROOT_URLCONF = 'mysite.urls'

MEDIA_ROOT = '/Users/rhzhang/Desktop/research proj/files/media'
MEDIA_URL = '/media/'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__)) + '/..'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

TEMPLATE_LOADERS = (

'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader', 

#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',

##     'django.template.loaders.eggs.load_template_source',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tutdb',
        'HOST': 'localhost',
        'USER': 'rhzhang',
        'PASSWORD': 'zhang647'
    }
}
'''
#

# Internationalization
# https://doc.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
