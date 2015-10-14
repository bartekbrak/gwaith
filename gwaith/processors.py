"""
Contains processors forming desired output of the scraped data.
"""
import csv
import json
import sys


def to_json(currency, rates):
    serializable = {date: str(rate) for date, rate in rates.items()}
    return json.dumps({currency: serializable})


def to_csv(currency, rates, writer=csv.writer(sys.stdout)):
    for date, rate in rates.items():
        writer.writerow([currency, date, rate])


def raw(currency, rates):
    return currency, rates


def raw_python(currency, rates):
    import dateutil.parser
    return currency, {
        dateutil.parser.parse(date): rate
        for date, rate in rates.items()
    }
