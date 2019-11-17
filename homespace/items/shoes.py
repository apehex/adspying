# -*- coding: utf-8 -*-

"""
=========
Shoes Ads
=========

Items scraped from shoes ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field
from scrapy.loader.processors import Identity, Join, TakeFirst

from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SHOES
#####################################################################

class ShoesAd(SecondHandAd):
    """
    """
    # Specifications
    category = Field() # sneakers, city, etc
    size = Field()

class ShoesAdLoader(SecondHandAdLoader):
    """
    """
    category_in = Join()
    category_out = Identity()

    size_in = Join()
    size_out = Identity()
