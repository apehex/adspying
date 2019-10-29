# -*- coding: utf-8 -*-

"""
=========
Leboncoin
=========

Customize the spiders for leboncoin.
"""

from __future__ import division, print_function, absolute_import

import urllib.parse
import re

import scrapy

from typical import checks

#####################################################################
# URL TEMPLATE
#####################################################################

BASE_URL = 'https://www.leboncoin.fr/recherche/?'

PRICE_VALUE_TEMPLATE = '{min}-{max}'

#####################################################################
# GENERIC ARGS
#####################################################################

CATEGORY_VALUES = {
    None: '',
    'appliances': '20',
    'caravaning': '4',
    'utility': '5', 
    'networking': '17',
    'real_estate': '9',
    'shoes': '53',
    'sports': '29',
}

LOCATION_VALUES = {
    None: '',
    'rhone_alpes': 'r_22'
}

PRICE_VALUES = {
    None: [],
    'appliances': (
        [0, 5]
        + list(range(10, 50, 10))
        + list(range(50, 100, 25))
        + list(range(100, 550, 100))),
    'caravaning': (
        list(range(0, 1000, 250))
        + list(range(1000, 3000, 500))
        + list(range(3000, 15000, 1000))
        + list(range(15000, 30000, 2500))
        + list(range(30000, 55000, 5000))),
    'networking': (
        [0, 5]
        + list(range(10, 50, 10))
        + list(range(50, 100, 25))
        + list(range(100, 550, 100))),
    'real_estate': [],
    'shoes': [],
    'sports': [],
}

#####################################################################
# VEHICULE ARGS
#####################################################################

URL_ARGS = {
    'result_page_number': 'o',
    'min_year': 'rs',
    'max_year': 're',
    'min_price': 'price=min-',
    'max_price': 'pe',
    'min_mileage': 'ms',
    'max_mileage': 'me',
    'fuel_type': 'fu'}

FUEL_ARG = {
    'petrol': 1,
    'diesel': 2,
    'lpg': 3,
    'electric': 4,
    'hybrid': 5}

# urllib.urlencode(url_args)

#####################################################################
# DATA SELECTION
#####################################################################

LISTING_ITEM_XPATH = (
    '//section[@id="container"]/main/div'
    + '/div[contains(@class,"_3iQ0i")]'
    + '/div[contains(@class,"l17WS")]/div'
    + '/div[contains(@class,"_2Njaz")]'
    + '/div[contains(@class,"_358dQ")]'
    + '/div/div/ul/li')
LISTING_ITEM_ATTRIBUTE_XPATH = {
    'image': 'a/div/span[contains(@class, "_a3cT")]/div/img/@src',
    'title': 'a/@title',
    'price': 'a/section[contains(@class, "_2EDA9")]/div/div/span/span[contains(@class, "_1NfL7")]/text()',
    'location': 'a/section[contains(@class, "_2EDA9")]/div/p[contains(@class,"_2qeuk")]/text()',
    'last_updated': 'a/section[contains(@class, "_2EDA9")]/div/p[contains(@class,"mAnae")]/text()',
    'url': 'a/@href',
}

ITEM_AD_XPATH = {
    'image': '',
    'title': '',
    'price': '',
    'location': '',
    'last_updated': '',
    'description': '',
}

#####################################################################
# STRIP IRRELEVANT CHARS
#####################################################################

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = [BASE_URL]

    def start_requests(self):
        """
        """
        __urls = [
            BASE_URL,
        ]
        __args = {
            'category': CATEGORY_VALUES[re.sub(
                '\W+',
                '',
                getattr(self, 'category', 'real_estate'))],
            'locations': LOCATION_VALUES[re.sub(
                '\W+',
                '',
                getattr(self, 'locations', 'rhone_alpes'))]}

        for __url in __urls:
            yield scrapy.Request(
                url=__url + urllib.parse.urlencode(__args),
                callback=self.parse)

    def parse(self, response):
        """
        """
        filename = 'leboncoin.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
