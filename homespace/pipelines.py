# -*- coding: utf-8 -*-

"""
=========
Pipelines
=========

Exporting data.
"""

from __future__ import division, print_function, absolute_import

from datetime import date
from functools import wraps
import os

from scrapy.exporters import CsvItemExporter
from scrapy.loader import ItemLoader

from typical import checks

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# ENABLE / DISABLE PIPELINES
#####################################################################

def toggle_pipeline(
        process_item_method: callable) -> callable:
    """
    This wrapper makes it so pipelines can be turned on and off at a spider level.
    """
    @wraps(process_item_method)
    def wrapper(self, item, spider):
        if self.__class__.__name__ in spider._pipelines:
            return process_item_method(self, item, spider)
        else:
            return item

    return wrapper

#####################################################################
# SECOND HAND ADS
#####################################################################

class SecondHandAdPipeline(object):

    def __init__(
            self,
            file_path):
        """
        """
        self.file_path = file_path

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
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
                '/homespace/',
                __spider_name,
                '{query}_{date}.csv'.format(
                    query=__query_name.replace('_', '-'),
                    date=date.today().strftime('%Y-%m-%d'))))

    def open_spider(
            self,
            spider):
        """
        """
        __file = open(self.file_path, 'wb')
        self.exporter = CsvItemExporter(
            file=__file,
            delimiter=',',
            join_multivalued=' ',
            include_headers_line=True)
        self.exporter.start_exporting()

    def close_spider(
            self,
            spider):
        """
        """
        self.exporter.finish_exporting()

    def process_item(
            self,
            item,
            spider):
        """
        """
        self.exporter.export_item(item)
        return item

#####################################################################
# LEGAL DOCUMENTS
#####################################################################

class LegalDocumentPipeline(object):

    def __init__(
            self,
            file_path):
        """
        """
        self.file_path = file_path

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
        __spider_name = 'none'
        if crawler.spider:
            __spider_name = getattr(
                crawler.spider,
                'name',
                'none')

        return cls(
            file_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                '/gdpr/',
                __spider_name))

    @toggle_pipeline
    def process_item(
            self,
            item,
            spider):
        """
        """
        __provider = ''.join(item.get(
            'provider',
            ['none']))
        __text = ''.join(item.get(
            'text',
            ['']))

        with open(
                os.path.join(
                    self.file_path,
                    __provider + '.html'),
                'w') as file:
            file.write(__text)

        return item
