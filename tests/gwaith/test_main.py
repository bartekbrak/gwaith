from unittest.mock import Mock, patch

from gwaith.main import get_all_rates


@patch('gwaith.main.get_currency_feed_urls', return_value={'PLN': 'url'})
@patch('gwaith.main.get_rates')
def test_get_all_rates(get_rates, get_currency_feed_urls):
    m_processor = Mock()
    for _ in get_all_rates(processor=m_processor):
        pass
    assert get_currency_feed_urls.called
    assert get_rates.called
    assert m_processor.called
