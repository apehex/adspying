# -*- coding: utf-8 -*-

"""
==============
smartphone Ads
==============

Items scraped from smartphones ads.
"""

from __future__ import division, print_function, absolute_import

from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SMARTPHONES
#####################################################################

class SmartphoneAd(SecondHandAd):
    """
    """
    # Specifications
    os = Field()
    ram = Field()
    ssd = Field()
    battery = Field()
    camera = Field()
    size = Field()
    weight = Field()

class SmartphoneAdLoader(SecondHandAdLoader):
    """
    """
    os_in = Join()
    os_out = Identity()

    ram_in = Join()
    ram_out = Identity()
    
    ssd_in = Join()
    ssd_out = Identity()
    
    battery_in = Join()
    battery_out = Identity()
    
    camera_in = Join()
    camera_out = Identity()
    
    size_in = Join()
    size_out = Identity()
    
    weight_in = Join()
    weight_out = Identity()
