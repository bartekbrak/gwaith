from setuptools import setup, find_packages


setup(
    name='gwaith',
    description='a standalone library to download European Central Bank '
                'foreign exchange reference rates',
    packages=find_packages(include=('gwaith*',)),
    version='2015.10.11.1',
    install_requires=[],
)