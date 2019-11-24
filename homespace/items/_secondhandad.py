# -*- coding: utf-8 -*-

"""
==============
Second Hand Ad
==============

Base class for all the specific ad items.
"""

from __future__ import division, print_function, absolute_import

from geopy.geocoders import Nominatim

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst

from homespace._wrangling import remove_extra_spacing

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
    latitude = Field()
    longitude = Field()
    age = Field()
    user_rating = Field()

class SecondHandAdLoader(ItemLoader):

    default_output_processor = TakeFirst()

    url_in = MapCompose(remove_extra_spacing)
    url_out = Join()

    vendor_in = MapCompose(remove_extra_spacing)
    vendor_out = Join()

    title_in = MapCompose(remove_extra_spacing)
    title_out = Join()

    price_in = TakeFirst()
    price_out = Join()

    condition_in = MapCompose(remove_extra_spacing)
    condition_out = Join()

    location_in = MapCompose(remove_extra_spacing)
    location_out = Join()

    first_posted_in = MapCompose(remove_extra_spacing)
    first_posted_out = Join()

    last_updated_in = MapCompose(remove_extra_spacing)
    last_updated_out = Join()

    description_in = MapCompose(remove_extra_spacing)
    description_out = Join()

    images_in = Join(', ')
    images_out = Join()

    brand_in = MapCompose(remove_extra_spacing)
    brand_out = Join()

    model_in = MapCompose(remove_extra_spacing)
    model_out = Join()

    make_in = MapCompose(remove_extra_spacing)
    make_out = Join()

    color_in = MapCompose(remove_extra_spacing)
    color_out = Join()

    price_new_in = MapCompose(remove_extra_spacing)
    price_new_out = Join()

    user_rating_in = MapCompose(remove_extra_spacing)
    user_rating_out = Join()

    def load_item(
            self):
        """
        """
        __item = super(SecondHandAdLoader, self).load_item()
        __geolocator = Nominatim(user_agent='homespace')
        __location = __geolocator.geocode(
            __item['location'],
            exactly_one=True)

        __item['latitude'] = __location.latitude
        __item['longitude'] = __location.longitude

        return __item
