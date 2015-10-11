"""
Contains functions doing simple scraping (as opposed to parsing the scraped
content and extracting the data in its desired format.

The scraping is based on regular expressions rather than on purpose built
HTML parsers (Beautiful Soup), to keep code small and dependence free.
"""
from gwaith.defaults import rss_page


def get_list_of_currency_feeds(url=rss_page):
    pass