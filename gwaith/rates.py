"""
Handler for getting rates from a single rss url and its helper funcitons.
"""
import feedparser


def _get_feed_entries(url):
    """
    Download whole feed from a given url and extract the part where the
    relevant informations is stored - entries.

    :param url: full url to a single RSS feed
    :return: list
    """
    complete_feed = feedparser.parse(url)
    return complete_feed.entries


def _get_rate_value(raw_rate):
    """
    Extract float rate value from a format like this '1.5853\nEUR'.

    :param raw_rate: str
    :return: float
    """
    return float(raw_rate.split('\n')[0])


def _get_rates(feed_entries):
    """
    Get a dict of parsed rates noted by a date from a list of feed entries.

    :param feed_entries: list of dicts
    :return: dict
    """
    relevant_parts = (
        (entry['updated'], entry['cb_exchangerate']) for entry in feed_entries
    )
    return {
        date: _get_rate_value(raw_rate)
        for date, raw_rate in relevant_parts
    }


def get_rates(url):
    """
    Handler for getting rates from a single rss url.

    :param url: full url to a single RSS feed
    :return: dict
    """
    entries = _get_feed_entries(url)
    return _get_rates(entries)
