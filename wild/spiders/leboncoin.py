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
# GENERIC ARGS
#####################################################################

LEBONCOIN_CATEGORIES = {
    None: '',
    'appliances': '20',
    'caravaning': '4',
    'networking': '17',
    'real_estate': '9',
    'shoes': '53',
    'sports': '29',
}

LEBONCOIN_LOCATIONS = {
    None: '',
    'rhone_alpes': 'r_22'
}

#####################################################################
# URL TEMPLATE
#####################################################################

LEBONCOIN_BASE_URL = 'https://www.leboncoin.fr/recherche/?'

LEBONCOIN_URL_ARGS = {
    'result_page_number': 'o',
    'min_year': 'rs',
    'max_year': 're',
    'min_price': 'price=min-',
    'max_price': 'pe',
    'min_mileage': 'ms',
    'max_mileage': 'me',
    'fuel_type': 'fu'}

LEBONCOIN_PRICE_ARG = {
    0: 0,
    1: 500,
    2: 1000,
    3: 2000,
    4: 3000,
    5: 4000,
    6: 5000,
    7: 6000,
    8: 7000,
    9: 8000,
    10: 9000,
    11: 10000,
    12: 15000,
    13: 20000,
    14: 30000,
    15: -1}

LEBONCOIN_FUEL_ARG = {
    'petrol': 1,
    'diesel': 2,
    'lpg': 3,
    'electric': 4,
    'hybrid': 5}

# urllib.urlencode(url_args)

#####################################################################
# DATA PARSING
#####################################################################

#This will create a list of buyers:
titles_xpath = '//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h2[@class="item_title"]/text()'
#This will create a list of prices
prices_xpath = '//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h3[@class="item_price"]/@content'
#The corresponding locations
cities_xpath = '//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/p[@itemprop="availableAtOrFrom"]/meta[1]/@content'
areas_xpath = '//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/p[@itemprop="availableAtOrFrom"]/meta[2]/@content'
#The creation dates
publication_dates_xpath = '//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/aside/p[@itemprop="availabilityStarts"]/@content'

#####################################################################
# STRIP IRRELEVANT CHARS
#####################################################################

# titles = [t.strip() for t in titles]

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = ['www.leboncoin.fr/recherche/?']

    def start_requests(self):
        """
        """
        __urls = [
            'http://www.leboncoin.fr/recherche/?',
        ]
        __args = {
            'category': LEBONCOIN_CATEGORIES[re.sub(
                '\W+',
                '',
                getattr(self, 'category', 'real_estate'))],
            'locations': LEBONCOIN_LOCATIONS[re.sub(
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
