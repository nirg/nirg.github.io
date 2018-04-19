#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nir Grinberg'
SITENAME = u'Three.Fourteen'
SITEURL = 'http://www.nirg.net'
SITEURL_ABS = SITEURL
RELATIVE_URLS = False

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Lazer Lab', 'http://lazerlab.net/'),
		  ('CS @ Cornell', 'http://www.cs.cornell.edu/'),
          ('Social Technologies Lab @ Cornell Tech', 'https://s.tech.cornell.edu/'),
          ('Facebook Core Data Science', 'https://research.facebook.com/datascience'),
          ('Harvard IQSS', 'http://www.iq.harvard.edu/'),
		  ('Network Science Institute', 'http://www.networkscienceinstitute.org/'))

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

ADDRESS = "177 Auntington Ave., 10th floor, Boston, MA 02115"
MAIL = "last.first name -AT- gmail.com"
TWITTER_USER = "grinbergnir"
GOOGLEPLUS_USER = "110010581376861389601"
LINKEDIN_USER = "nir-grinberg/44/23b/15"
FACEBOOK_USER = "nirgr"
ABOUT_TEXT = "Any text set here will show up on the bottom right of the page."
ABOUT_IMAGE = "/images/portrait_sq.jpg"
ABOUT_LINK = "/pages/about.html"
COPYRIGHT = "Nir Grinberg 2018"
#SHOW_COPYRIGHT : True by default, you can set it to False to hide the copyrights.

MENUITEMS = [('Home', '/index.html'), ('Blog', '/blog.html')]

TEMPLATE_PAGES = {'../theme/templates/blog.html': 'blog.html'}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['summary']

DISQUS_SITENAME = 'threefourteen'
GOOGLE_ANALYTICS = 'UA-49475310-1'
TWITTER_CARDS = True
OPEN_GRAPH_IMAGE = "images/portrait_sq.jpg"
