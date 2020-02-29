# -*- coding: utf-8 -*-

"""
===============
Real-Estate Ads
===============

Items scraped from real-estate ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field
from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst

from homespace._wrangling import format_datetime, remove_all_spacing, remove_extra_spacing, extract_area_value
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

    # Transactions
    fees_included = Field()

    # Computed
    time_to_work = Field()
    buildable = Field()

class RealEstateAdLoader(SecondHandAdLoader):
    """
    """
    # Specifications
    category_in = Identity()
    category_out = Join()

    rooms_in = MapCompose(remove_all_spacing, int)
    rooms_out = Join()

    floors_in = MapCompose(remove_all_spacing, int)
    floors_out = Join()

    indoor_area_in = MapCompose(remove_extra_spacing, extract_area_value)
    indoor_area_out = Join()

    outdoor_area_in = MapCompose(remove_extra_spacing, extract_area_value)
    outdoor_area_out = Join()

    energy_grade_in = MapCompose(remove_extra_spacing)
    energy_grade_out = Join()

    ghg_grade_in = MapCompose(remove_extra_spacing)
    ghg_grade_out = Join()

    # Transactions
    fees_included_in = MapCompose(remove_extra_spacing)
    fees_included_out = Join()

    # Computed
    time_to_work_in = MapCompose(remove_extra_spacing)
    time_to_work_out = Join()

    buildable_in = MapCompose(remove_extra_spacing)
    buildable_out = Join()

    def load_item(
            self):
        """
        Complete the raw information with computed data.
        """
        __item = super(RealEstateAdLoader, self).load_item()

        # evaluation & sorting depend on the query
        __item['value_rating'] = 5 # neutral value
        __item['leverage_rating'] = 5 # neutral value

        # summary
        __item['summary'] = (
            'price: ' + serialize_html_tag('<strong>', str(__item.get('price', ''))) + '<br />'
            + 'indoor area: ' + serialize_html_tag('<strong>', str(__item.get('indoor_area', ''))) + ' m²<br />'
            + 'outdoor area: ' + serialize_html_tag('<strong>', str(__item.get('outdoor_area', ''))) + ' m²<br />'
            + 'rooms: ' + serialize_html_tag('<strong>', str(__item.get('rooms', ''))) + '<br />'
            + 'floors: ' + serialize_html_tag('<strong>', str(__item.get('floors', ''))) + '<br />'
            + 'energy grade: ' + serialize_html_tag('<strong>', str(__item.get('energy_grade', ''))) + '<br />'
            + 'value: ' + serialize_html_tag('<strong>', str(__item.get('value_rating', ''))) + ' / 10<br />'
            + 'leverage: ' + serialize_html_tag('<strong>', str(__item.get('leverage_rating', ''))) + ' / 10<br />'
            + 'age: ' + serialize_html_tag('<strong>', str(__item.get('age', ''))) + ' days<br />')

        return __item
