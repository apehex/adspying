# -*- coding: utf-8 -*-

"""
=============
Scraped Items
=============

Items scraped from second hand ads.
"""

from __future__ import division, print_function, absolute_import

import scrapy

#####################################################################
# COMPUTER
#####################################################################

class ComputerAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_updated = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    ram_model = scrapy.Field()
    ram_size = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class LaptopAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_updated = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    ram_model = scrapy.Field()
    ram_size = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class MotherBoardAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_updated = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    chipset = scrapy.Field()
    bus = scrapy.Field()
    size = scrapy.Field()
    ethernet = scrapy.Field()
    wifi = scrapy.Field()
    graphics = scrapy.Field()
    connections = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class GraphicsCardAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    gpu_frequency = scrapy.Field()
    gpu_cores = scrapy.Field()
    ram_frequency = scrapy.Field()
    ram_size = scrapy.Field()
    port = scrapy.Field()
    connections = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class HardDriveAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class SolidStateDriveAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class RamAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class PowerSupplyAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    power = scrapy.Field()
    noise = scrapy.Field()
    size = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

class CasingAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Specifications
    outside_size = scrapy.Field()
    motherboard_size = scrapy.Field()
    connections = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()
