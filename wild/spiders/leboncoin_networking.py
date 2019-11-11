# -*- coding: utf-8 -*-

"""
=====================
Leboncoin Real-Estate
=====================

Search for real-estate in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

from wild.items import SmartphoneAd, SmartphoneAdLoader
from wild.spiders.leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

BRAND_VALUES = []

COLOR_VALUES = []

MODEL_VALUES = []

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100)))

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSmartphoneSpider(LeboncoinSpider):
    name = 'leboncoin_smartphone'
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSmartphoneSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '17',
            'locations': '',
            'page': '1',
            'phone_brand': '',
            'phone_color': '',
            'phone_memory': '',
            'phone_model': '',
            'price': '',
            'shippable': '1',
            'text': ''}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'brand': (
                '//div[contains(@data-qa-id, "criteria_item_phone_brand")]'
                + '/div/div[2]/text()'),
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_phone_color")]'
                + '/div/div[2]/text()'),
            'model': (
                '//div[contains(@data-qa-id, "criteria_item_phone_model")]'
                + '/div/div[2]/text()'),
            'ram': (
                '//div[contains(@data-qa-id, "criteria_item_phone_memory")]'
                + '/div/div[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = SmartphoneAd
        self._loader_class = SmartphoneAdLoader
