import csv
import datetime
import json
import sys
from collections import OrderedDict

import pip
import pytest

from gwaith.processors import raw, raw_python, to_csv, to_json

currency = 'GBP'
# makes testing hardcoded output predictable, easier
rates = OrderedDict([
    ('2015-10-06T14:15:00+01:00', 0.7399),
    ('2015-10-07T14:15:00+01:00', 0.7358),
    ('2015-10-09T14:15:00+01:00', 0.7407),
    ('2015-10-12T14:15:00+01:00', 0.7401),
    ('2015-10-08T14:15:00+01:00', 0.7366),
])


def test_to_json():
    result = json.loads(to_json(currency, rates))
    expected = {currency: rates}
    assert result == expected


def test_to_csv(capfd):
    to_csv(currency, rates, writer=csv.writer(sys.stdout, dialect='unix'))
    out, err = capfd.readouterr()
    expected = (
        '"GBP","2015-10-06T14:15:00+01:00","0.7399"\n'
        '"GBP","2015-10-07T14:15:00+01:00","0.7358"\n'
        '"GBP","2015-10-09T14:15:00+01:00","0.7407"\n'
        '"GBP","2015-10-12T14:15:00+01:00","0.7401"\n'
        '"GBP","2015-10-08T14:15:00+01:00","0.7366"\n'
    )
    assert out == expected
    assert err == ''


def test_raw():
    result_currency, result_rates = raw(currency, rates)
    assert result_currency == currency
    assert result_rates == rates


@pytest.mark.skipif(
    'python-dateutil' not in
    [_.key for _ in pip.get_installed_distributions()],
    reason='requires python-dateutil'
)
def test_raw_python():
    result_currency, result_rates = raw_python(currency, rates)
    assert result_currency == currency
    for date, rate in result_rates.items():
        assert isinstance(date, datetime.datetime)
        assert isinstance(rate, float)
