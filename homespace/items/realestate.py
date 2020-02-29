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

from homespace._wrangling import format_datetime, format_text, remove_all_spacing, extract_area_value, serialize_html_tag
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
    price_per_square_meter = Field()
    time_to_work = Field()
    buildable = Field()

class RealEstateAdLoader(SecondHandAdLoader):
    """
    """
    # Specifications
    category_in = Identity()
    category_out = Join()

    rooms_in = MapCompose(format_text, remove_all_spacing, int)
    rooms_out = TakeFirst()

    floors_in = MapCompose(format_text, remove_all_spacing, int)
    floors_out = TakeFirst()

    indoor_area_in = MapCompose(format_text, extract_area_value)
    indoor_area_out = TakeFirst()

    outdoor_area_in = MapCompose(format_text, extract_area_value)
    outdoor_area_out = TakeFirst()

    energy_grade_in = MapCompose(format_text)
    energy_grade_out = Join()

    ghg_grade_in = MapCompose(format_text)
    ghg_grade_out = Join()

    # Transactions
    fees_included_in = MapCompose(format_text)
    fees_included_out = Join()

    # Computed
    time_to_work_in = MapCompose(format_text)
    time_to_work_out = Join()

    buildable_in = MapCompose(format_text)
    buildable_out = Join()

    def load_item(
            self):
        """
        Complete the raw information with computed data.
        """
        __item = super(RealEstateAdLoader, self).load_item()

        if __item.get('price', 0) > 0 and __item.get('indoor_area', 0) > 0:
            __item['price_per_square_meter'] = __item['price'] / __item['indoor_area']

        # evaluation & sorting depend on the query
        __item['value_rating'] = 5 # neutral value
        __item['leverage_rating'] = 5 # neutral value

        # summary
        __item['summary'] = (
            'price: ' + serialize_html_tag('<i>', str(__item.get('price', ''))) + ' €<br />'
            + 'indoor area: ' + serialize_html_tag('<i>', str(__item.get('indoor_area', ''))) + ' m²<br />'
            + 'outdoor area: ' + serialize_html_tag('<i>', str(__item.get('outdoor_area', ''))) + ' m²<br />'
            + 'rooms: ' + serialize_html_tag('<i>', str(__item.get('rooms', ''))) + '<br />'
            + 'floors: ' + serialize_html_tag('<i>', str(__item.get('floors', ''))) + '<br />'
            + 'energy grade: ' + serialize_html_tag('<i>', str(__item.get('energy_grade', ''))) + '<br />'
            + 'value: ' + serialize_html_tag('<i>', str(__item.get('value_rating', ''))) + ' / 10<br />'
            + 'leverage: ' + serialize_html_tag('<i>', str(__item.get('leverage_rating', ''))) + ' / 10<br />'
            + 'age: ' + serialize_html_tag('<i>', str(__item.get('age', ''))) + ' days<br />')

        return __item
