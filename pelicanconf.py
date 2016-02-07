#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Richard Ree'
SITENAME = u'Ree Lab @ The Field Museum'
SITETITLE = u'Ree Lab @ The Field Museum'
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

THEME = 'Flex'
## THEME = 'pure-single'
## THEME = 'theme/pelican-free-agent-master'

COVER_IMG_URL = '/images/pedicularis-bella.jpg'
TAGLINE = 'systematics, evolution, biogeography'
SOCIAL = (
    ('github', 'https://github.com/rhr'),
)
