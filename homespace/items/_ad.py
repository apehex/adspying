# -*- coding: utf-8 -*-

"""
==============
Second Hand Ad
==============

Base class for all the specific ad items.
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
