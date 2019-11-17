# -*- coding: utf-8 -*-

"""
==============
Appliances Ads
==============

Items scraped from appliances ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field
from scrapy.loader.processors import Identity, Join, TakeFirst

from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# APPLIANCES
#####################################################################

class AppliancesAd(SecondHandAd):
    """
    """
    # Specifications
    pass

class AppliancesAdLoader(SecondHandAdLoader):
    """
    """
    pass
