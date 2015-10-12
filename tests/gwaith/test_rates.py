from unittest.mock import patch

import pytest

from gwaith.rates import (
    _get_feed_entries,
    _get_rate_value,
    _get_rates,
    get_rates
)


def _test_get_feed_entries(entries):
    assert entries
    assert len(entries) == 5
    for entry in entries:
        assert 'cb_exchangerate' in entry
        assert 'updated' in entry


@pytest.mark.online
def test_get_feed_entries():
    url = 'https://www.ecb.europa.eu/rss/fxref-pln.html'
    entries = _get_feed_entries(url)
    _test_get_feed_entries(entries)


def test_get_feed_entries_offline():
    rss_file = open('tests/data/fxref-pln.html').read()
    entries = _get_feed_entries(rss_file)
    _test_get_feed_entries(entries)


def test_get_rate_value():
    assert _get_rate_value('1.5853\nEUR') == 1.5853


def test__get_rates():
    entries_part = [
        {'cb_exchangerate': '1.5502\nEUR',
         'updated': '2015-10-09T14:15:00+01:00'},
        {'cb_exchangerate': '1.5664\nEUR',
         'updated': '2015-10-08T14:15:00+01:00'},
        {'cb_exchangerate': '1.5586\nEUR',
         'updated': '2015-10-07T14:15:00+01:00'},
        {'cb_exchangerate': '1.5781\nEUR',
         'updated': '2015-10-06T14:15:00+01:00'},
        {'cb_exchangerate': '1.5853\nEUR',
         'updated': '2015-10-05T14:15:00+01:00'}
    ]
    rates = _get_rates(entries_part)
    assert set([e['updated'] for e in entries_part]) == set(rates.keys())
    assert all(isinstance(item, float) for item in rates.values())


@patch('gwaith.rates._get_feed_entries')
@patch('gwaith.rates._get_rates')
def test_get_rates(m_get_rates, m_get_feed_entries):
    get_rates(None)
    assert m_get_rates.called
    assert m_get_feed_entries.called
