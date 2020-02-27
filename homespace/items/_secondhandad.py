# -*- coding: utf-8 -*-

"""
==============
Second Hand Ad
==============

Base class for all the specific ad items.
"""

from __future__ import division, print_function, absolute_import

from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst

from homespace._wrangling import format_datetime, remove_extra_spacing

#####################################################################
# SERIALIZE DATETIMES
#####################################################################

def parse_datetime(
        text: str,
        loader_context: dict) -> str:
    """
    Format the dates according to ISO 8601.

    The loader context is setup by the crawler to match the formating
    of its target website.

    Parameters
    ----------
    text: str.
        The serialized datetime, as displayed on the website.
    loader_context: dict.
        The item load context.

    Results
    -------
    out: str.
        The serialized datetime, in ISO 8601 format.
    """
    return format_datetime(
        string=text,
        format=loader_context.get('datetime_format', '%Y-%m-%dT%H:%M:%S'))

#####################################################################
# GENERIC AD
#####################################################################

class SecondHandAd(Item):
    """
    Generic ad item, composed of:
    - ad information
    - vendor information
    - item information
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
    age = Field() # in days
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

    first_posted_in = MapCompose(remove_extra_spacing, parse_datetime)
    first_posted_out = Join()

    last_updated_in = MapCompose(remove_extra_spacing, parse_datetime)
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
        Complete the information available on the web with
        computed data.
        """
        __item = super(SecondHandAdLoader, self).load_item()
        __geolocator = Nominatim(user_agent='homespace')
        __location = __geolocator.geocode(
            __item.get('location', 'north pole'),
            exactly_one=True)

        # gps coordinates
        __item['latitude'] = __location.latitude
        __item['longitude'] = __location.longitude

        # timeline
        __item['first_posted'] = __item['last_updated']
        __item['age'] = (
            datetime.now()
            - datetime.strptime(
                __item.get(
                    'last_updated',
                    datetime.now().isoformat(sep='T', timespec='seconds')),
                '%Y-%m-%dT%H:%M:%S')).days

        return __item
