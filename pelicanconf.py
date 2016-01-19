#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Richard Ree'
SITENAME = u'The Ree Lab @ Field Museum'
SITEURL = ''

THEME='theme/pelican-free-agent-master'
THEME_STATIC_DIR = 'theme'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
## SOCIAL = (('You can add links in your config file', '#'),
##           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

DEFAULT_CATEGORY = 'news'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index']
# Top Menu Links
NAVLINKS = (
	#('#page-top', 'Home'),
	('#news','News'),
	('#research','Research'),
	('#publications','Publications'),
	('#software','Software'),
	('#people','People'),
	## ('#portfolio', 'Portfolio'),
	## ('#about', 'About'),
	## ('#contact', 'Contact')
)

# Portfolio Name
#PORTFOLIO = 'Recent publications'

#Contact form fields sorted by: label, input_type, id, required_validation_,msg
## CONTACT_FIELDS = (
## 	['Name', 'text', 'name', 'Please enter your name.'],
## 	['Email Address', 'email', 'email','Please enter your email address.' ],

## 	['Message', 'textarea', 'message', 'Please enter a message.']
## )
