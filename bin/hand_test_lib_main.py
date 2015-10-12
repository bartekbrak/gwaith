#!/usr/bin/env python
import csv
import sys

from gwaith import get_rates, processors

only = ('PLN', 'GBP')

for data in get_rates(processor=processors.to_json, only=only):
    print(data)

for data in get_rates(processor=processors.raw, only=only):
    print(data)

for data in get_rates(processor=processors.raw_python, only=only):
    print(data)

for data in get_rates(processor=processors.raw_python, only=only):
    print(data)
writer = csv.writer(sys.stdout)
writer.writerow(['Currency', 'Date', 'Rate'])
for currency in get_rates(
        processor=processors.to_csv, only=only, writer=writer):
    # silly, isn't it, the to_csv might need rethinking, I guess
    pass
