# -*- coding: utf-8 -*-

"""
===========
Real-Estate
===========

Search for real-estate in ad listings.
"""

from __future__ import division, print_function, absolute_import

from homespace.items.realestate import RealEstateAd, RealEstateAdLoader
from homespace.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 375000, 25000))
    + list(range(400000, 700000, 50000))
    + list(range(700000, 1500000, 100000))
    + [1500000, 2000000])

ROOMS_VALUES = list(range(1, 9, 1))

SQUARE_VALUES = (
    list(range(20, 160, 10))
    + [200, 300, 500])

TYPE_VALUES = ['old', 'new', 'viager']

#####################################################################
# SPIDER
#####################################################################

class LeboncoinRealEstateSpider(LeboncoinSpider):
    name = 'leboncoin_realestate'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinRealEstateSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '9',
                'immo_sell_type': '',
                'locations': '',
                'owner_type': '', # private / pro
                'page': '1',
                'real_estate_type': '',
                'rooms': '',
                'shippable': '',
                'square': '',
                'price': '',
                'text': ''},
            'farmily': {
                'category': '9',
                'immo_sell_type': '',
                'locations': '',
                'page': '1',
                'real_estate_type': '1',
                'rooms': '2-max',
                'shippable': '',
                'square': '60-max',
                'price': 'min-250000',
                'text': ''},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'category': (
                '//div[contains(@data-qa-id, "criteria_item_real_estate_type")]'
                + '/div/div[2]/text()'),
            'energy_grade': (
                '//div[contains(@data-qa-id, "criteria_item_energy_rate")]'
                + '/div/div[2]/div'
                + '/div[contains(@class, "_1sd0z")]/text()'),
            'fees_included': (
                '//div[contains(@data-qa-id, "criteria_item_fai_included")]'
                + '/div/div[2]/text()'),
            'ghg_grade': (
                '//div[contains(@data-qa-id, "criteria_item_ges")]'
                + '/div/div[2]/div'
                + '/div[contains(@class, "_1sd0z")]/text()'),
            'indoor_area': (
                '//div[contains(@data-qa-id, "criteria_item_square")]'
                + '/div/div[2]/text()'),
            'rooms': (
                '//div[contains(@data-qa-id, "criteria_item_rooms")]'
                + '/div/div[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = RealEstateAd
        self._loader_class = RealEstateAdLoader
