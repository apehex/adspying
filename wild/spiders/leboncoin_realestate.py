# -*- coding: utf-8 -*-

"""
=====================
Leboncoin Real-Estate
=====================

Search for real-estate in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

from wild.items import RealEstateAd, RealEstateAdLoader
from wild.spiders.leboncoin import LeboncoinSpider

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
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinRealEstateSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '9',
            'immo_sell_type': '',
            'locations': '',
            'page': '1',
            'real_estate_type': '',
            'rooms': '',
            'shippable': '1',
            'square': '',
            'price': '',
            'text': ''}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'category': (
                '//div[contains(@data-qa-id, "criteria_item_real_estate_type")]'
                + '/div/div[2]/text()'),
            'energy_grade': (
                '//div[contains(@data-qa-id, "criteria_item_energy_rate")]'
                + '/div/div[2]/div'
                + '/div[contains(@class, "_1sd0z")]/text()'),
            'fees': (
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
