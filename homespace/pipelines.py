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

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# URL TEMPLATE
#####################################################################


class SecondHandAdPipeline(object):

    def __init__(self, file_path):
        self.file_path = file_path

    @classmethod
    def from_crawler(cls, crawler):
        __spider_name = 'none'
        __query_name = 'none'
        if crawler.spider:
            __spider_name = getattr(
                crawler.spider,
                'name',
                'none')
            __query_name = getattr(
                crawler.spider,
                'query',
                'none')

        return cls(
            file_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                __spider_name,
                '{query}_{date}.csv'.format(
                    query=__query_name.replace('_', '-'),
                    date=date.today().strftime('%Y-%m-%d'))))

    def open_spider(self, spider):
        __file = open(self.file_path, 'wb')
        self.exporter = CsvItemExporter(
            file=__file,
            delimiter=',',
            join_multivalued=' ',
            include_headers_line=True,
            fields_to_export=(
                list(spider._ad_generic_attributes_xpath.keys())
                + list(spider._ad_specific_attributes_xpath.keys())))
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
