"""
Contains functions doing simple scraping and their helper functions (as
opposed to parsing the scraped content and extracting the data in its desired
format).

The scraping is based on regular expressions rather than on purpose built
HTML parsers (Beautiful Soup), to keep code small and dependence free.

"""
import re
from functools import lru_cache
from urllib.request import urlopen

from .defaults import RE_rss_href, ecb_page


@lru_cache(maxsize=2)
def _get_currency_feed_html(url):
    """

    :param url: full URL to ECB RSS news feeds website.
    :return: str
    """
    return urlopen(url).read().decode('utf-8')


@lru_cache(maxsize=2)
def _get_currency_feed_urls(html):
    """
    Return a cached dictionary of currency names and full URLs.

    :param html: str containg HTML of the ECB feeds site
    :return: dict
    """

    feeds = re.findall(RE_rss_href, html)
    return {currency.upper(): ecb_page + path for path, currency in feeds}


def get_currency_feed_urls(url, only=None):
    """
    Return a (limited) dictionary of currency names and full URLs.

    :param url: full URL to ECB RSS news feeds website.
    :param only: a sequence of string, in ISO 4217 currency codes form,
                 like 'PLN', used for narrowing down results
    :return:
    """
    html = _get_currency_feed_html(url)
    return {
        currency: url for currency, url in
        _get_currency_feed_urls(html).items()
        if (only and currency in only) or not only
        }
