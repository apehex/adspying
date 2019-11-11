# -*- coding: utf-8 -*-

"""
===============
Leboncoin Shoes
===============

Search for shoes in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

import re
from urllib.parse import urlencode, urljoin

import scrapy

from wild.items import ShoesAd, ShoesAdLoader
from wild.spiders.leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

CATEGORY_VALUES = {
    'baskets sneakers': 'basket',
    'chaussures lacets': 'lacet',
    'chaussures scratch': 'scratch',
    'mocassins': 'mocassin',
    'bottines lowboots': 'bottine',
    'bottes': 'botte',
    'escarpins': 'escarpin',
    'sandales nu-pieds': 'sandale',
    'chaussons pantoufles': 'chausson',
    'ballerines': 'ballerine',
    'autres': 'autre'
}

PRICE_VALUES = (
    list(range(0, 30, 5))
    + [40, 50, 100, 250])

SIZE_VALUES = {
    '41': '26' # eu: cm
}

TYPE_VALUES = {
    'women': '1',
    'men': '2',
    'children': '3'}

#####################################################################
# SPIDER
#####################################################################

class LeboncoinShoesSpider(LeboncoinSpider):
    name = 'leboncoin_shoes'
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(MySpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '53'
            'page': '1',
            'shippable': '1',
            'shoe_category_a': '',
            'shoe_size': '',
            'shoe_type': '',
            'price': '',
            'text': ''}

        # scrape the resulting listing
        self._specific_ad_attributes_xpath = {
            'category': (
                '//div[contains(@data-qa-id, "criteria_item_shoe_category")]'
                + '/div/div[2]/text()'),
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_clothing_color")]'
                + '/div/div[2]/text()'),
            'size': (
                '//div[contains(@data-qa-id, "criteria_item_shoe_size")]'
                + '/div/div[2]/text()'),
            # 'type': (
            #     '//div[contains(@data-qa-id, "criteria_item_shoe_type")]'
            #     + '/div/div[2]/text()'), # men / women, mostly useless
        }

        # classes to store, clean and export the data
        self._item_class = ShoesAd
        self._loader_class = ShoesAdLoader
