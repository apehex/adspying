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

#####################################################################
# SMARTPHONES
#####################################################################

class SmartphoneAd(scrapy.Item):
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
    os = scrapy.Field()
    ram = scrapy.Field()
    ssd = scrapy.Field()
    battery = scrapy.Field()
    camera = scrapy.Field()
    size = scrapy.Field()
    weight = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VanAd(scrapy.Item):
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
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    consumption = scrapy.Field()
    size_inside = scrapy.Field()
    size_outside = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

#####################################################################
# REAL ESTATE
#####################################################################

class HomeAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    location = scrapy.Field()

    # Specifications
    rooms = scrapy.Field()
    floors = scrapy.Field()
    indoor_area = scrapy.Field()
    outdoor_area = scrapy.Field()
    energy_grade = scrapy.Field()

    # Computed
    age = scrapy.Field()
    distance_to_work = scrapy.Field()

class LandAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_post = scrapy.Field()
    last_update = scrapy.Field()
    description = scrapy.Field()

    # Generic
    location = scrapy.Field()

    # Specifications
    area = scrapy.Field()
    buildable = scrapy.Field()

    # Computed
    age = scrapy.Field()
    distance_to_work = scrapy.Field()
