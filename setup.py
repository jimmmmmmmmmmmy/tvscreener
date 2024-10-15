from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '1.0.00'
DESCRIPTION = 'TradingView Screener API'
LONG_DESCRIPTION = 'Python library to retrieve screen for stock data from TV Screener'

# Setting up
setup(
    name="tvscreener",
    url="https://github.com/jimmmmmmmmmmmy/tvscreener",
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="House of AI",
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['pandas', 'requests>=2.27.1'],
    keywords='',
    python_requires='>=3.10',
)
