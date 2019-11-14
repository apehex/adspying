# -*- coding: utf-8 -*-

"""
================
Leboncoin Sportss
================

Search for sport items in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

from wild.items import SportsAd, SportsAdLoader
from wild.spiders.leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100))
    + [1000])

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSportsSpider(LeboncoinSpider):
    name = 'leboncoin_sports'
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSportsSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '29',
            'locations': '',
            'page': '1',
            'price': '',
            'shippable': '1',
            'text': (
                'ski%20randonnée'
                + '%20-enfant'
                + '%20-pantalon%20-combinaison%20-masque%20-gant%20-blouson')}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = SportsAd
        self._loader_class = SportsAdLoader
