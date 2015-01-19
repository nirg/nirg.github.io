#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nir Grinberg'
SITENAME = u'Three.Fourteen'
SITEURL = 'http://www.nirg.net'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('CS @ Cornell', 'http://www.cs.cornell.edu/'),
          ('Social Media Info. Lab @ Rutgers', 'http://sm.rutgers.edu/'))

# Social widget
SOCIAL = (('Github', 'https://github.com/nirg'),
          ('Twitter', 'https://twitter.com/grinbergnir'),
          ('Linkedin', 'http://www.linkedin.com/pub/nir-grinberg/44/23b/15'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'papers','files', 'files/upenn2014/social-media-diurnal-patterns.html']
ARTICLE_EXCLUDES = ['files', 'files/upenn2014']

THEME = "theme"

ADDRESS = "111 8th Ave. Suite 302, New York, NY 10011"
MAIL = "nir -AT- cs.cornell.edu"
TWITTER_USER = "grinbergnir"
GOOGLEPLUS_USER = "110010581376861389601"
LINKEDIN_USER = "nir-grinberg/44/23b/15"
FACEBOOK_USER = "nirgr"
ABOUT_TEXT = "Any text set here will show up on the bottom right of the page."
ABOUT_IMAGE = "/images/Clymer_N0130_5624-sci.jpg"
ABOUT_LINK = "/pages/about.html"
COPYRIGHT = "Nir Grinberg 2014"
#SHOW_COPYRIGHT : True by default, you can set it to False to hide the copyrights.

MENUITEMS = [('Home', '/index.html'), ('Blog', '/blog.html')]

TEMPLATE_PAGES = {'../theme/templates/blog.html': 'blog.html'}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['summary']

DISQUS_SITENAME = 'threefourteen'
GOOGLE_ANALYTICS = 'UA-49475310-1'
