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
# GENERIC AD
#####################################################################

class SecondHandAd(scrapy.Item):
    """
    """
    # Ad
    title = scrapy.Field()
    price = scrapy.Field()
    first_posted = scrapy.Field()
    last_updated = scrapy.Field()
    description = scrapy.Field()

    # Generic
    vendor = scrapy.Field()
    model = scrapy.Field()
    make = scrapy.Field()
    price_new = scrapy.Field()

    # Additional
    user_rating = scrapy.Field()

#####################################################################
# COMPUTER
#####################################################################

class ComputerAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = scrapy.Field()
    ram_size = scrapy.Field()

class LaptopAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = scrapy.Field()
    ram_size = scrapy.Field()

class MotherBoardAd(SecondHandAd):
    """
    """
    # Specifications
    chipset = scrapy.Field()
    bus = scrapy.Field()
    size = scrapy.Field()
    ethernet = scrapy.Field()
    wifi = scrapy.Field()
    graphics = scrapy.Field()
    connections = scrapy.Field()

class GraphicsCardAd(SecondHandAd):
    """
    """
    # Specifications
    gpu_frequency = scrapy.Field()
    gpu_cores = scrapy.Field()
    ram_frequency = scrapy.Field()
    ram_size = scrapy.Field()
    port = scrapy.Field()
    connections = scrapy.Field()

class HardDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

class SolidStateDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

class RamAd(SecondHandAd):
    """
    """
    # Specifications
    speed = scrapy.Field()
    size = scrapy.Field()
    technology = scrapy.Field()

class PowerSupplyAd(SecondHandAd):
    """
    """
    # Specifications
    power = scrapy.Field()
    noise = scrapy.Field()
    size = scrapy.Field()

class CasingAd(SecondHandAd):
    """
    """
    # Specifications
    outside_size = scrapy.Field()
    motherboard_size = scrapy.Field()
    connections = scrapy.Field()

#####################################################################
# SMARTPHONES
#####################################################################

class SmartphoneAd(SecondHandAd):
    """
    """
    # Specifications
    os = scrapy.Field()
    ram = scrapy.Field()
    ssd = scrapy.Field()
    battery = scrapy.Field()
    camera = scrapy.Field()
    size = scrapy.Field()
    weight = scrapy.Field()

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VanAd(SecondHandAd):
    """
    """
    # Specifications
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    consumption = scrapy.Field()
    size_inside = scrapy.Field()
    size_outside = scrapy.Field()

#####################################################################
# REAL ESTATE
#####################################################################

class HomeAd(SecondHandAd):
    """
    """
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
    time_to_work = scrapy.Field()

class LandAd(SecondHandAd):
    """
    """
    # Generic
    location = scrapy.Field()

    # Specifications
    area = scrapy.Field()
    buildable = scrapy.Field()

    # Computed
    age = scrapy.Field()
    time_to_work = scrapy.Field()
