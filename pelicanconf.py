#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Richard Ree'
SITENAME = u'Ree Lab @ The Field Museum'
SITETITLE = u'Ree Lab @ Field Museum'
SITEURL = 'http://localhost:8000'
SITELOGO = '/images/pedicularis-bella.jpg'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
## LINKS = (('Pelican', 'http://getpelican.com/'),
##          ('Python.org', 'http://python.org/'),
##          ('Jinja2', 'http://jinja.pocoo.org/'),
##          ('You can modify those links in your config file', '#'),)

# Social widget
## SOCIAL = (('You can add links in your config file', '#'),
##           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = (
    ('Research','pages/research'),
    ('Publications','pages/publications'),
    ('Software','pages/software'),
    )

## LOAD_CONTENT_CACHE = False

THEME = 'theme/BT3-Flat'
## THEME = 'Flex'
## THEME = 'pure-single'
## THEME = 'theme/pelican-free-agent-master'

BACKGROUND_IMAGE = '/images/pedicularis-bella.jpg'
SITESUBTITLE = 'systematics, evolution, biogeography'
SOCIAL = (
    ('github', 'https://github.com/rhr'),
)
POST_LIMIT = 3

ABOUT_TITLE = "systematics, evolution, biogeography"
HEADER_IMAGE = '/images/pedicularis-bella-small-square.jpg'
TEMPLATE_PAGES = {
    'blog.html': 'blog.html',
    ## 'publications.html': 'publications.html'
    }
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['pelican_bibtex']
PUBLICATIONS_SRC = 'content/mypubs.bib'

GSCHOLAR = 'https://scholar.google.com/citations?user=YeHSu8AAAAAJ'
