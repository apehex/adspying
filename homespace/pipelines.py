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

from homespace.items import SecondHandAd, SecondHandAdLoader

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

        return cls(
            file_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                __spider_name,
                '{date}.csv'.format(
                    date=date.today().strftime('%Y-%m-%d'))))

    def open_spider(self, spider):
        __file = open(self.file_path, 'wb')
        self.exporter = CsvItemExporter(
            file=__file,
            delimiter=',',
            join_multivalued=' ',
            include_headers_line=True,
            fields_to_export=(
                list(spider.AD_GENERIC_ATTRIBUTES_XPATH.keys())
                + list(spider._ad_specific_attributes_xpath.keys())))
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
