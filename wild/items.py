# -*- coding: utf-8 -*-

"""
=============
Scraped Items
=============

Items scraped from second hand ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, Join, TakeFirst

#####################################################################
# GENERIC AD
#####################################################################

class SecondHandAd(Item):
    """
    """
    # Ad
    url = Field()
    title = Field()
    price = Field()
    condition = Field()
    location = Field()
    first_posted = Field()
    last_updated = Field()
    description = Field()
    images = Field()

    # Generic
    vendor = Field()
    model = Field()
    make = Field()
    price_new = Field()

    # Additional
    user_rating = Field()

class SecondHandAdLoader(ItemLoader):

    default_output_processor = TakeFirst()

    url_in = TakeFirst()
    url_out = Identity()

    title_in = Join()
    title_out = Identity()

    price_in = TakeFirst()
    price_out = Identity()

    condition_in = Join()
    condition_out = Identity()

    location_in = Join()
    location_out = Identity()

    first_posted_in = Identity()
    first_posted_out = Identity()

    last_updated_in = Join()
    last_updated_out = Identity()

    description_in = Join()
    description_out = Identity()

    images_in = Join(', ')
    images_out = Identity()

    vendor_in = Identity()
    vendor_out = Identity()

    model_in = Identity()
    model_out = Identity()

    make_in = Identity()
    make_out = Identity()

    price_new_in = Identity()
    price_new_out = Identity()

    user_rating_in = Identity()
    user_rating_out = Identity()

#####################################################################
# COMPUTER
#####################################################################

class ComputerAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = Field()
    ram_size = Field()

class LaptopAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = Field()
    ram_size = Field()

class MotherBoardAd(SecondHandAd):
    """
    """
    # Specifications
    chipset = Field()
    bus = Field()
    size = Field()
    ethernet = Field()
    wifi = Field()
    graphics = Field()
    connections = Field()

class GraphicsCardAd(SecondHandAd):
    """
    """
    # Specifications
    gpu_frequency = Field()
    gpu_cores = Field()
    ram_frequency = Field()
    ram_size = Field()
    port = Field()
    connections = Field()

class HardDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class SolidStateDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class RamAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class PowerSupplyAd(SecondHandAd):
    """
    """
    # Specifications
    power = Field()
    noise = Field()
    size = Field()

class CasingAd(SecondHandAd):
    """
    """
    # Specifications
    outside_size = Field()
    motherboard_size = Field()
    connections = Field()

#####################################################################
# SHOES
#####################################################################

class ShoesAd(SecondHandAd):
    """
    """
    # Specifications
    category = Field() # sneakers, city, etc
    color = Field()
    size = Field()

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

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VanAd(SecondHandAd):
    """
    """
    # Specifications
    fuel = Field()
    mileage = Field()
    consumption = Field()
    size_inside = Field()
    size_outside = Field()

#####################################################################
# REAL ESTATE
#####################################################################

class HomeAd(SecondHandAd):
    """
    """
    # Generic
    location = Field()

    # Specifications
    rooms = Field()
    floors = Field()
    indoor_area = Field()
    outdoor_area = Field()
    energy_grade = Field()

    # Computed
    age = Field()
    time_to_work = Field()

class LandAd(SecondHandAd):
    """
    """
    # Generic
    location = Field()

    # Specifications
    area = Field()
    buildable = Field()

    # Computed
    age = Field()
    time_to_work = Field()
