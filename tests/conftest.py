"""
py.test configuration

Currently allows reporting on lru_cache usage
"""


def pytest_terminal_summary(terminalreporter):
    reporter = terminalreporter
    from gwaith.scrapers import (
        _get_currency_feed_html,
        _get_currency_feed_urls,
    )
    cached_functions = [_get_currency_feed_html, _get_currency_feed_urls]
    reporter.write_sep('-', 'lru_cache usage:')
    for f in cached_functions:
        line = '%s: %s' % (f.__wrapped__.__name__, f.cache_info())
        reporter.write_line(line)
