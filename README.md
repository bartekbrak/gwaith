# Gwaith

A standalone library to download European Central Bank foreign exchange
reference rates.

This library was written as a showcase piece of code for a prospective
employer. It is not intended to be used in production environment, however,
it may work. Use at your own discretion.

# Usage

```python
from gwaith import ECBDownloader

rates = ECBDownloader().download()
```

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
```

# Contributing

I do not plan to expand the library, so fork the code and treat as your own.

# Code structore
`gwaith` contains the library, `bin` convenience shell scripts.

# Licence

Released under MIT License.