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
from inspect import getfullargspec
import os

from scrapy.exporters import CsvItemExporter
from scrapy.loader import ItemLoader

from typical import checks

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# ENABLE / DISABLE PIPELINES
#####################################################################

@checks
def _empty_open_spider(
        self,
        spider):
    """
    Alternative "open_spider" method, as replacement when the pipeline
    is not enabled for the current spider. 
    """
    pass

@checks
def _empty_close_spider(
        self,
        spider):
    """
    Alternative "close_spider" method, as replacement when the pipeline
    is not enabled for the current spider.
    """
    pass

@checks
def _empty_process_item(
        self,
        item,
        spider):
    """
    Alternative "process_item" method, as replacement when the pipeline
    is not enabled for the current spider.
    """
    return item

@checks
def redirects(
        pipeline_method: callable) -> callable:
    """
    This decorator turns pipeline methods on/off depending
    on the current spider.

    In practice, it replaces the wrapped method with an
    empty one if the conditions are not met.
    """
    __arg_spec = getfullargspec(pipeline_method)

    if pipeline_method.__name__ == 'open_spider':
        @wraps(pipeline_method)
        def open_spider_wrapper(self, spider):
            if self.__class__.__name__ in spider._pipelines:
                return pipeline_method(self, spider)
            else:
                return _empty_open_spider(self, spider)
        return open_spider_wrapper

    elif pipeline_method.__name__ == 'close_spider':
        @wraps(pipeline_method)
        def close_spider_wrapper(self, spider):
            if self.__class__.__name__ in spider._pipelines:
                return pipeline_method(self, spider)
            else:
                return _empty_close_spider(self, spider)
        return close_spider_wrapper

    elif pipeline_method.__name__ == 'process_item':
        @wraps(pipeline_method)
        def process_item_wrapper(self, item, spider):
            if self.__class__.__name__ in spider._pipelines:
                return pipeline_method(self, item, spider)
            else:
                return _empty_process_item(self, item, spider)
        return process_item_wrapper

    return pipeline_method

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
                'homespace/',
                __spider_name,
                '{query}_{date}.csv'.format(
                    query=__query_name.replace('_', '-'),
                    date=date.today().strftime('%Y-%m-%d'))))

    @redirects
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

    @redirects
    def close_spider(
            self,
            spider):
        """
        """
        self.exporter.finish_exporting()

    @redirects
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
                'gdpr/',
                __spider_name))

    @redirects
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
