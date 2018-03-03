#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Collect ads from Leboncoin."""

from lxml import html
import requests
import urllib

LEBONCOIN_BASE_URL = 'https://www.leboncoin.fr/utilitaires/offres/?'

LEBONCOIN_URL_ARGS = {
    'result_page_number': 'o',
    'min_year': 'rs',
    'max_year': 're',
    'min_price': 'ps',
    'max_price': 'pe',
    'min_mileage': 'ms',
    'max_mileage': 'me',
    'fuel_type': 'fu'}

LEBONCOIN_PRICE_DICT = {
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

LEBONCOIN_FUEL_DICT = {
        'petrol': 1,
        'diesel': 2,
        'lpg': 3,
        'electric': 4,
        'hybrid': 5}



PAGE = requests.get(LEBONCOIN_BASE_URL)
TREE = html.fromstring(PAGE.content)

#This will create a list of buyers:
TITLES = TREE.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h2[@class="item_title"]/text()')
#This will create a list of prices
PRICES = TREE.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h3[@class="item_price"]/text()')

print TITLES[2]
print PRICES[2]
