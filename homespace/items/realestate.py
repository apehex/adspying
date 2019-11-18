# -*- coding: utf-8 -*-

"""
===============
Real-Estate Ads
===============

Items scraped from real-estate ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field
from scrapy.loader.processors import Identity, Join, TakeFirst

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

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
