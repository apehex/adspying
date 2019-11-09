# -*- coding: utf-8 -*-

"""
=========
Pipelines
=========

Exporting data.
"""

from __future__ import division, print_function, absolute_import

from datetime import date
import os
import re

import scrapy
from scrapy.exporters import CsvItemExporter
from scrapy.loader import ItemLoader

from typical import checks

from wild.items import SecondHandAd, SecondHandAdLoader

#####################################################################
# URL TEMPLATE
#####################################################################


class SecondHandAdPipeline(object):

    def __init__(self, file_path):
        self.file_path = file_path

    @classmethod
    def from_crawler(cls, crawler):
        __spider_name = 'none'
        __ad_category = 'none'
        if crawler.spider:
            __spider_name = crawler.spider.name
            __ad_category = crawler.spider.category

        return cls(
            file_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                '{date}_{spider}_{category}.csv'.format(
                    date=date.today().strftime('%Y-%m-%d'),
                    spider=__spider_name,
                    category=__ad_category)))

    def open_spider(self, spider):
        __file = open(self.file_path, 'wb')
        self.exporter = CsvItemExporter(
            file=__file,
            delimiter=',',
            join_multivalued=' ',
            include_headers_line=True,
            fields_to_export=[
                'url',
                'title',
                'price',
                'condition',
                'location',
                'first_posted',
                'last_updated',
                'description',
                'images',
                'vendor',
                'model',
                'make',
                'price_new',
                'user_rating'])
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
