# -*- coding: utf-8 -*-

"""
==============
Legal Document
==============

Base class for all the specific legal documents.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst

from homespace._wrangling import extract_text_from_html_markup

#####################################################################
# GENERIC AD
#####################################################################

class LegalDocument(Item):
    """
    """
    # Source
    url = Field()
    title = Field()
    provider = Field()
    last_updated = Field()

    # Document
    text = Field()

class LegalDocumentLoader(ItemLoader):

    default_output_processor = TakeFirst()

    url_in = TakeFirst()
    url_out = Identity()

    title_in = Join()
    title_out = Identity()

    provider_in = Join()
    provider_out = Identity()

    last_updated_in = Join()
    last_updated_out = Identity()

    text_in = MapCompose(extract_text_from_html_markup)
    text_out = Join()
