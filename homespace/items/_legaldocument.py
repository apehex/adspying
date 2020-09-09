# -*- coding: utf-8 -*-

"""
==============
Legal Document
==============

Base class for all the specific legal documents.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy import Field, Item
from scrapy.loader import ItemLoader

from homespace._wrangling import prettify_html

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

    url_in = Identity()
    url_out = Join()

    title_in = Identity()
    title_out = Join()

    provider_in = Identity()
    provider_out = Join()

    last_updated_in = Identity()
    last_updated_out = Join()

    text_in = MapCompose(prettify_html)
    text_out = Join()
