# Gwaith

A standalone library to download European Central Bank foreign exchange
reference rates.

This library was written as a showcase piece of code for a prospective
employer. It is not intended to be used in production environment, however,
it may work. Use at your own discretion. Due to the nature of the motivation
for writing this library it is at times arguably over-complicated and against
YAGNI principle. No Python Zen monks were actually harmed in the process.

# Usage

```python
from gwaith import get_rates

for rates in get_rates():
    print(rates)

# or
only = ('PLN', 'GBP')
for data in get_rates(processor=processors.to_json, only=only):
    print(data)

# or see bin/hand_test_lib_main.py for usage examples

```

## Processors

Tiny functions allowing you to return the data in some common formats. Feel
free to write your own. Have a look at `gwaith.processors` to understand the
API.

# Install

## In production

From GitHub only, there are no plans to release it to PyPi.

```bash
pip install git+ssh://git@github.com/bartekbrak/gwaith.git
```

# For development

```bash
git clone git@github.com:bartekbrak/gwaith.git
cd gwaith
pip install -e . -r dev_requirements.txt
```

# Run tests

```bash
pip install -r dev_requirements.txt
py.test
# run tests connecting to the Internet
py.test -m 'online'
# also have a look in setup.cfg to learn the hardcoded py.test args
```

# Known issues:
The library makes a few assumtions about the data that ECB provides 
that might not hold and would require extra live testing:

- Currency feeds provide rates on distinct dates, if this 
  breaks and two identical dates are provided, the earlier will be forgotten 
- The CSV processor creates a generator, this for the sake of the API cosistency
  but this processor does not return anything, it writes directly to the object
  provided, be it stdout or file, this might be surprising to the end user

# Contributing

I do not plan to expand the library, so fork the code and treat as your own.

# Code structore
`gwaith` contains the library, `bin` convenience shell scripts.

# Licence

Released under MIT License.
