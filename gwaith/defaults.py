"""
Gathers configuration strings for the whole project. Anything used as a
default will be stored here. This is the single source of truth about the lib
configuration. The defaults shall be overridable in their respective use
points.
"""
ecb_page = 'http://www.ecb.europa.eu'
rss_page = ecb_page + '/home/html/rss.en.html'

RE_rss_href = 'href=\"(?P<href>/rss/fxref-(?P<currency>\w+).html)'
