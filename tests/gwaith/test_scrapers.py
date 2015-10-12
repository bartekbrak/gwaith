import re
from unittest.mock import patch

from gwaith import scrapers
from gwaith.defaults import ecb_page
from gwaith.scrapers import (
    _get_currency_feed_html,
    _get_currency_feed_urls,
    get_currency_feed_urls
)


html = '''
<ul class="zebraList">
    <li><a class="rss" href="/rss/fxref-pln.html">Polish zloty (PLN)</a></li>
    <li><a class="rss" href="/rss/fxref-ron.html">Romanian leu (RON)</a></li>
</ul>
    '''


@patch('gwaith.scrapers.urlopen')
def test_get_currency_feed_html(urlopen):
    assert scrapers.urlopen is urlopen
    _get_currency_feed_html(None)
    assert urlopen.called


def test__get_list_of_currency_feeds():
    feeds = _get_currency_feed_urls(html)
    assert len(feeds) == 2
    for cur in ('PLN', 'RON'):
        assert cur in feeds
    for feed in feeds.values():
        assert re.search(ecb_page + '/rss/fxref-\w+.html', feed)


@patch('gwaith.scrapers._get_currency_feed_html', return_value=html)
def test_get_currency_feed_urls(_get_currency_feed_html):
    feed = get_currency_feed_urls(None, only=['RON'])
    assert _get_currency_feed_html.called
    assert feed == {'RON': 'http://www.ecb.europa.eu/rss/fxref-ron.html'}
