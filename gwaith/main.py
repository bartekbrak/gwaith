"""
Contains a function implementing the main logic, combining all the other parts.
"""
from . import processors
from .defaults import rss_page
from .rates import get_rates
from .scrapers import get_currency_feed_urls


def get_all_rates(url=rss_page, processor=processors.raw, only=None,
                  **processor_kwargs):
    """
    Get ECB foreign currency exchange rates to EUR.
    :param url: full URL to ECB RSS news feeds website.
    :param processor: decides the output format, see processors
    :param only: sequence, limit list of currencies
    :param processor_args:
    :return:
    """
    feed_urls = get_currency_feed_urls(url, only)
    for currency, feed_url in feed_urls.items():
        rates = get_rates(feed_url)
        yield processor(currency, rates, **processor_kwargs)
