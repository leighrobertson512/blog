#!/usr/bin python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wray Mills'
SITENAME = u'The Art of Technology... Training'
SITEURL = u'http://blog.techemstudios.com'

THEME = "themes/nest"

TIMEZONE = u'US/Eastern'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = u'%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = ((u'Tech Em', u'http://techemstudios.com'),
             (u'About', u'http://techemstudios.com/about-us'))

# Blogroll
LINKS =  ((u'Tech Em Studios', u'http://techemstudios.com'),
          (u'Register!',u'http://register.techemstudios.com'),
          (u'Enrollment',u'https://secure.techemstudios.com'),
          (u'Python.org', u'http://python.org/'),
          (u'Pelican', u'http://getpelican.com'),)

# Social widget
SOCIAL = ((u'@TechEmRVA', u'http://twitter.com/techemrva'),
          (u'TechEm on GitHub',u'https://github.com/techemstudios'),
          (u'TechEm on FB', u'http://facebook.com/techemstudios'),)

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GITHUB_URL = u'https://github.com/techemstudios'

# Dopetrope
ADDRESS = u'1123 Gaskins, Rd., Suite 600B'
MAIL = u'info@techemstudios.com'
TWITTER_USER = u'TechEmRVA'
FACEBOOK_USER = u'techemstudios'
COPYRIGHT = u'techemstudios'
ABOUT_IMAGE = u'images/icon.png'
ABOUT_LINK = u'http://techemstudios.com/about-us.html'
SHOW_COPYRIGHT = True

# Nest
NEST_HEADER_IMAGES = u'raspberry-pi-stock.jpg'
NEST_HEADER_LOGO = u'/images/small-icon.png'
NEST_INDEX_HEAD_TITLE = u'Tech Em Blog'
NEST_INDEX_HEADER_TITLE = u'Tech Em Blog'
NEST_INDEX_HEADER_SUBTITLE = u'Be more than a user of technology'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
