from setuptools import find_packages, setup

setup(
    name='gwaith',
    description='a standalone library to download European Central Bank '
                'foreign exchange reference rates',
    packages=find_packages(include=('gwaith*',)),
    version='2015.10.12.6',
    author='Bartek Brak',
    author_email='bartek.rychlicki@gmail.com',
    install_requires=[
        'feedparser==5.2.1',
    ],
    extras_require={
        'processors': ['python-dateutil==2.4.2']
    }
)
