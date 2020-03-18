#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Analysis North'
SITENAME = u'Analysis North'
SITEURL = 'http://analysisnorth.com'

DISQUS_SITENAME = 'analysisnorthblog'

TIMEZONE = 'US/Alaska'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ('index', 'tags', 'archives')

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

FILENAME_METADATA = '(?P<slug>.*)'

# Menu Items
MENUITEMS = ( ('Home', '/'),
              ('AkWarm', '/AkWarm/AkWarm2download.html'),
              ('Services', '/pages/services.html'),
              ('Projects', '/pages/projects.html'),
              ('Articles', '/category/articles.html'),
              ('Solar Data', '/enphase/solar_summary.html'),
              ('About', '/pages/about.html'),
              ('Contact', '/pages/contact.html'),
            )

# Blogroll
LINKS =  (('Python Programming Language', 'http://python.org/'),
          ('Pandas Data Analysis', 'http://pandas.pydata.org/'),
          ('Raspberry Pi $35 Linux Computer', 'http://www.raspberrypi.org/'),
          ('Adafruit Electronic Products','http://www.adafruit.com/'), 
          ('Sparkfun Electronic Products', 'https://www.sparkfun.com/'),
          ('Ride1Up Electric Bicycles', 'https://ride1up.com/?wpam_id=69'),
         )

# Social widget
SOCIAL = (('Alan Mitchell on LinkedIn', 'http://www.linkedin.com/pub/alan-mitchell/59/759/a80'),
          ('Alan Mitchell on GitHub', 'https://github.com/alanmitchell'),
          )

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 100

# Had to add to fix a bug related to not generating pages.
PATH = 'content'

# Totally Clears output directory when building.  ** CAREFUL **
DELETE_OUTPUT_DIRECTORY = True

# Disable the Authors page
AUTHORS_SAVE_AS = False
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

# Save articles in a subdirectory
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

THEME = 'pelican-themes-Alan/zurb-F5-basic-mod01'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
