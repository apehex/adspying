# -*- coding: utf-8 -*-

"""
=====================
Leboncoin Real-Estate
=====================

Search for real-estate in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

from wild.items import VehiculeAd, VehiculeAdLoader
from wild.spiders.leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

FUEL_VALUES = []

MAKE_VALUES = list(range(1960, 2020, 1))

MILEAGE_VALUES = (
    list(range(0, 100000, 10000))
    + list(range(100000, 275000, 25000)))

PRICE_VALUES = (
    list(range(0, 1000, 250))
    + list(range(1000, 3000, 500))
    + list(range(3000, 15000, 1000))
    + list(range(15000, 30000, 2500))
    + list(range(30000, 55000, 5000)))

#####################################################################
# SPIDER
#####################################################################

class LeboncoinVehiculeSpider(LeboncoinSpider):
    name = 'leboncoin_vehicule'
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinVehiculeSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '5', # utility vehicules
            'fuel': '',
            'locations': '',
            'mileage': '',
            'page': '1',
            'price': '',
            'regdate': '',
            'shippable': '1',
            'text': ''}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'fuel': (
                '//div[contains(@data-qa-id, "criteria_item_fuel")]'
                + '/div/div[2]/text()'),
            'gearbox': (
                '//div[contains(@data-qa-id, "criteria_item_gearbox")]'
                + '/div/div[2]/text()'),
            'make': (
                '//div[contains(@data-qa-id, "criteria_item_regdate")]'
                + '/div/div[2]/text()'),
            'mileage': (
                '//div[contains(@data-qa-id, "criteria_item_mileage")]'
                + '/div/div[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = VehiculeAd
        self._loader_class = VehiculeAdLoader
