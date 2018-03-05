#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Collect ads from Leboncoin."""

from __future__ import absolute_import, division, print_function
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

page = requests.get(LEBONCOIN_BASE_URL)
tree = html.fromstring(page.content)

# urllib.urlencode(url_args)

#####################################################################
# QUERY LEBONCOIN
#####################################################################

#This will create a list of buyers:
titles = tree.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h2[@class="item_title"]/text()')
#This will create a list of prices
prices = tree.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h3[@class="item_price"]/@content')
#The corresponding locations
cities = tree.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/p[@itemprop="availableAtOrFrom"]/meta[1]/@content')
areas = tree.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/p[@itemprop="availableAtOrFrom"]/meta[2]/@content')
#The creation dates
publication_dates = tree.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/aside/p[@itemprop="availabilityStarts"]/@content')

#####################################################################
# STRIP IRRELEVANT CHARS
#####################################################################

titles = [t.strip() for t in titles]

#####################################################################
# TRANSLATE IN REFERENTIAL TERMS
#####################################################################

#TODO : areas to fr department code
#TODO : cities to fr postal code

print(titles[2])
print(prices[2])
print(cities[2])
print(areas[2])
print(publication_dates[2])

# TODO
# strip spaces, tabs, symbols etc
# extract
#   manufacturer (from csv)
#   model (from csv)
#   price
# calculate the age of the ad
