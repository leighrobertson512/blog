#!/usr/bin python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wray Mills'
SITENAME = u'The Art of Technology... Training'
SITEURL = 'http://blog.techemstudios.com'

THEME = "themes/html5-dopetrope"

TIMEZONE = u'US/Eastern'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = u'%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = (('Tech Em', 'http://techemstudios.com'),
             ('About', 'http://techemstudios.com/about-us'))

# Blogroll
LINKS =  (('Tech Em Studios', 'http://techemstudios.com'),
          ('Python.org', 'http://python.org/'),
          ('Pelican', 'http://getpelican.com'),)

# Social widget
SOCIAL = (('@TechEmRVA', 'http://twitter.com/techemrva'),
          ('TechEm Studios on FB', 'http://facebook.com/techemstudios'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_URL = u'https://github.com/techemstudios'

ADDRESS = u'1123 Gaskins, Rd., Suite 600B'
MAIL = u'info@techemstudios.com'
TWITTER_USER = u'TechEmRVA'
FACEBOOK_USER = u'techemstudios'
COPYRIGHT = u'techemstudios'
ABOUT_IMAGE = u'images/icon.png'
ABOUT_LINK = u'http://techemstudios.com/about-us.html'
SHOW_COPYRIGHT = True
