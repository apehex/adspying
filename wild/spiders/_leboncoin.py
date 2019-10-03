# -*- coding: utf-8 -*-

"""
=========
Leboncoin
=========

Customize the spiders for leboncoin.
"""

from __future__ import division, print_function, absolute_import

import urllib.parse

from typical import checks

#####################################################################
# REFERENTIALS
#####################################################################

LEBONCOIN_CATEGORIES = {
    None: '',
    'caravaning': '4',
    'real_estate': '9'
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
