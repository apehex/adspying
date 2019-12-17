# -*- coding: utf-8 -*-

"""
===========
Sports Gear
===========

Search for sports gear items in ad listings.
"""

from __future__ import division, print_function, absolute_import

from homespace.items.sports_gear import SportsGearAd, SportsGearAdLoader
from homespace.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100))
    + [1000])

#####################################################################
# FILTERS
#####################################################################

SKIS_FILTER = (
    'ski randonnée'
    + ' -enfant'
    + ' -pantalon -combinaison -masque -gant -blouson')
ICE_AXE_FILTER = ('')

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSportsGearSpider(LeboncoinSpider):
    name = 'leboncoin_sports_gear'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSportsGearSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '29',
                'locations': '',
                'page': '1',
                'price': '',
                'search_in': '',
                'shippable': '1',
                'text': ''},
            'hardshell_jacket': {
                'category': '29',
                'locations': 'r_30',
                'page': '1',
                'price': 'min-200',
                'search_in': '',
                'shippable': '1',
                'text': SKIS_FILTER},
            'ice_axe': {
                'category': '29',
                'locations': 'r_30',
                'page': '1',
                'price': 'min-200',
                'search_in': '',
                'shippable': '1',
                'text': SKIS_FILTER},
            'skis': {
                'category': '29',
                'locations': 'r_30',
                'page': '1',
                'price': 'min-200',
                'search_in': '',
                'shippable': '1',
                'text': SKIS_FILTER},
            'ski_boots': {
                'category': '29',
                'locations': 'r_30',
                'page': '1',
                'price': 'min-200',
                'search_in': '',
                'shippable': '1',
                'text': SKIS_FILTER}
            'ski_fixations': {
                'category': '29',
                'locations': 'r_30',
                'page': '1',
                'price': 'min-200',
                'search_in': '',
                'shippable': '1',
                'text': SKIS_FILTER},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = SportsGearAd
        self._loader_class = SportsGearAdLoader
