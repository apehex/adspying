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

from homespace.exporters import GeoJsonItemExporter, HtmlItemExporter
from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# ENABLE / DISABLE PIPELINES
#####################################################################

@checks
def _redirects_open_spider(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "open_spider" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    @wraps(pipeline_method)
    def open_spider_wrapper(self, spider):
        if self.__class__.__name__ in spider._pipelines:
            return pipeline_method(self, spider)
        else:
            return (lambda __self, __spider: None)(self, spider)
    return open_spider_wrapper

@checks
def _redirects_close_spider(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "close_spider" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    return _redirects_open_spider(pipeline_method)

@checks
def _redirects_process_item(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "process_item" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    @wraps(pipeline_method)
    def process_item_wrapper(self, item, spider):
        if self.__class__.__name__ in spider._pipelines:
            return pipeline_method(self, item, spider)
        else:
            return (lambda __self, __item, __spider: __item)(
                self, item, spider)
    return process_item_wrapper

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
        return _redirects_open_spider(pipeline_method)
    elif pipeline_method.__name__ == 'close_spider':
        return _redirects_close_spider(pipeline_method)
    elif pipeline_method.__name__ == 'process_item':
        return _redirects_process_item(pipeline_method)

    return pipeline_method

#####################################################################
# BASE
#####################################################################

class BasePipeline(object):

    def __init__(
            self,
            parent_path,
            file_name,
            file_extension='.txt'):
        """
        """
        self._file_path = os.path.join(
            parent_path,
            file_name + file_extension)
        self._file = open(self._file_path, 'wb')

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
        __project_name = 'homespace'
        __spider_name = 'default'
        __query_name = 'default'
        if crawler.spider:
            __project_name = getattr(
                crawler.spider,
                'project',
                'homespace')
            __spider_name = getattr(
                crawler.spider,
                'name',
                'default')
            __query_name = getattr(
                crawler.spider,
                'query',
                'default')

        return cls(
            parent_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                __project_name,
                __spider_name),
            file_name='{query}_{date}'.format(
                query=__query_name.replace('_', '-'),
                date=date.today().strftime('%Y-%m-%d')))

    @redirects
    def close_spider(
            self,
            spider):
        """
        """
        if self.exporter:
            self.exporter.finish_exporting()
        if not self._file.closed:
            self._file.close()

    @redirects
    def process_item(
            self,
            item,
            spider):
        """
        """
        if self.exporter:
            self.exporter.export_item(item)
        return item

#####################################################################
# CSV
#####################################################################

class CsvPipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(CsvPipeline, self).__init__(parent_path, file_name, '.csv')

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        if self._file:
            self.exporter = CsvItemExporter(
                file=self._file,
                delimiter=',',
                join_multivalued=' ',
                include_headers_line=True)
            self.exporter.start_exporting()

#####################################################################
# HTML
#####################################################################

class HtmlTablePipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(HtmlTablePipeline, self).__init__(parent_path, file_name, '.html')

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        if self._file:
            self.exporter = HtmlItemExporter(
                file=self._file,
                join_multivalued=' ',
                include_headers_line=True)
            self.exporter.start_exporting()

#####################################################################
# JSON
#####################################################################

class JsonPipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(JsonPipeline, self).__init__(parent_path, file_name, '.json')

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        if self._file:
            self.exporter = GeoJsonItemExporter(
                file=self._file)
            self.exporter.start_exporting()

#####################################################################
# RAW
#####################################################################

class RawPipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(RawPipeline, self).__init__(parent_path, file_name, '.txt')

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
                    os.path.dirname(self._file_path),
                    __provider + '.html'),
                'w') as __file:
            __file.write(__text)

        return item
