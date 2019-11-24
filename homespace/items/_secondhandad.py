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
    url_out = Join()

    vendor_in = Identity()
    vendor_out = Join()

    title_in = Identity()
    title_out = Join()

    price_in = TakeFirst()
    price_out = Join()

    condition_in = Identity()
    condition_out = Join()

    location_in = Identity()
    location_out = Join()

    first_posted_in = Identity()
    first_posted_out = Join()

    last_updated_in = Identity()
    last_updated_out = Join()

    description_in = Identity()
    description_out = Join()

    images_in = Join(', ')
    images_out = Join()

    brand_in = Identity()
    brand_out = Join()

    model_in = Identity()
    model_out = Join()

    make_in = Identity()
    make_out = Join()

    color_in = Identity()
    color_out = Join()

    price_new_in = Identity()
    price_new_out = Join()

    user_rating_in = Identity()
    user_rating_out = Join()
