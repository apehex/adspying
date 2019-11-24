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
    category_in = Identity()
    category_out = Join()

    rooms_in = Identity()
    rooms_out = Join()

    floors_in = Identity()
    floors_out = Join()

    indoor_area_in = Identity()
    indoor_area_out = Join()

    outdoor_area_in = Identity()
    outdoor_area_out = Join()

    energy_grade_in = Identity()
    energy_grade_out = Join()

    ghg_grade_in = Identity()
    ghg_grade_out = Join()

    time_to_work_in = Identity()
    time_to_work_out = Join()

    buildable_in = Identity()
    buildable_out = Join()
