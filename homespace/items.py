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
    vendor = Field()
    title = Field()
    price = Field()
    condition = Field()
    location = Field()
    first_posted = Field()
    last_updated = Field()
    description = Field()
    images = Field()

    # Generic
    brand = Field()
    model = Field()
    make = Field()
    color = Field()
    price_new = Field()

    # Additional
    age = Field()
    user_rating = Field()

class SecondHandAdLoader(ItemLoader):

    default_output_processor = TakeFirst()

    url_in = TakeFirst()
    url_out = Identity()

    vendor_in = Identity()
    vendor_out = Identity()

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

    brand_in = Identity()
    brand_out = Identity()

    model_in = Identity()
    model_out = Identity()

    make_in = Identity()
    make_out = Identity()

    color_in = Join()
    color_out = Identity()

    price_new_in = Identity()
    price_new_out = Identity()

    user_rating_in = Identity()
    user_rating_out = Identity()

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

#####################################################################
# COMPUTER
#####################################################################

class ComputerAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = Field()
    ram_size = Field()

class ComputerAdLoader(SecondHandAdLoader):
    """
    """
    ram_model_in = Join()
    ram_model_out = Identity()

    ram_size_in = Join()
    ram_size_out = Identity()

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
    size = Field()

class ShoesAdLoader(SecondHandAdLoader):
    """
    """
    category_in = Join()
    category_out = Identity()

    size_in = Join()
    size_out = Identity()

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

#####################################################################
# SPORTS
#####################################################################

class SportsGearAd(SecondHandAd):
    """
    """
    # Specifications
    pass

class SportsGearAdLoader(SecondHandAdLoader):
    """
    """
    pass

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VehiculeAd(SecondHandAd):
    """
    """
    # Specifications
    fuel = Field()
    mileage = Field()
    consumption = Field()
    size_inside = Field()
    size_outside = Field()

class VehiculeAdLoader(SecondHandAdLoader):
    """
    """
    # Specifications
    fuel_in = Join()
    fuel_out = Identity()

    mileage_in = Join()
    mileage_out = Identity()

    consumption_in = Join()
    consumption_out = Identity()

    size_inside_in = Join()
    size_inside_out = Identity()

    size_outside_in = Join()
    size_outside_out = Identity()

#####################################################################
# REAL ESTATE
#####################################################################

class RealEstateAd(SecondHandAd):
    """
    """
    # Specifications
    category = Field()
    rooms = Field()
    floors = Field()
    indoor_area = Field()
    outdoor_area = Field()
    energy_grade = Field()
    ghg_grade = Field()

    # Computed
    time_to_work = Field()
    buildable = Field()

class RealEstateAdLoader(SecondHandAdLoader):
    """
    """
    category_in = Join()
    category_out = Identity()

    rooms_in = Join()
    rooms_out = Identity()

    floors_in = Join()
    floors_out = Identity()

    indoor_area_in = Join()
    indoor_area_out = Identity()

    outdoor_area_in = Join()
    outdoor_area_out = Identity()

    energy_grade_in = Join()
    energy_grade_out = Identity()

    ghg_grade_in = Join()
    ghg_grade_out = Identity()

    time_to_work_in = Join()
    time_to_work_out = Identity()

    buildable_in = Join()
    buildable_out = Identity()
