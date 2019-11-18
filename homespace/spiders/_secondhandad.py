# -*- coding: utf-8 -*-

"""
=====================
Second Hand Ad Spider
=====================

Base class for scraping second hand ads.

This parent class outlines the processing of ad listings:
- define the search queries
- 
"""

from __future__ import division, print_function, absolute_import

from urllib.parse import urlencode, urljoin

import scrapy

from typical import checks

from homespace.cli import remove_special_characters
from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SPIDER
#####################################################################

class SecondHandAdSpider(scrapy.Spider):
    name = 'second_hand_ad'

    #################################################################
    # CLI
    #################################################################

    def _select_current_query(
            self):
        """
        Select the query to be executed.
        """
        self._current_query_name = getattr(
            self,
            'query',
            'default')
        self._current_query_args = self._queries.get(self._current_query_name)

    def _fill_current_query_args_with_cli_args(
            self):
        """
        Clean, format and translate to match the leboncoin url referential.
        """
        for __key, __value in self._current_query_args.items():
            self._current_query_args[__key] = getattr(
                self,
                __key,
                __value) # default to the current value

    def _set_stop_conditions(
            self):
        """
        Define when the scraping should stop:
        - after x pages of listing
        - when the listed ads get older than y
        """
        self._max_pages = int(getattr(
            self,
            'pages',
            '1'))

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(SecondHandAdSpider, self).__init__(*args, **kwargs)

        # stop condition
        self._max_pages = 1
        self._max_age = 1 # in days

        # url template
        self._base_url = ''
        self._search_page_url = ''

        # forge a query
        self._queries = {}
        self._current_query_name = 'default'
        self._current_query_args = {}

        # select data specific to a given ad search (say smartphones)
        self._ad_listing_xpath = ''
        self._ad_listing_attributes_xpath = {}
        self._ad_xpath = ''
        self._ad_generic_attributes_xpath = {}
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader

    def start_requests(self):
        """
        """
        # translate the cli args to the url std for leboncoin
        self._set_stop_conditions()
        self._select_current_query()
        self._fill_current_query_args_with_cli_args()

        # forge the search urls & queue the requests
        for i in range(self._max_pages):
            self._current_query_args['page'] = str(i + 1)
            yield scrapy.Request(
                url=urljoin(
                    self._base_url,
                    self._search_page_url.format(urlencode(self._current_query_args))),
                callback=self.parse_listing,
                meta={'page': str(i+1)})

    def parse_listing(self, response):
        """
        """
        __page = response.meta.get(
            'page',
            '1')
        __ad_links = response.xpath(
            self._ad_listing_xpath).xpath(
            self._ad_listing_attributes_xpath['url']).getall()

        for __link in __ad_links:
            yield scrapy.Request(
                url=urljoin(self._base_url, __link),
                callback=self.parse_item)

        self.log('[Page {page}] {count} ads queued...'.format(
            page = __page,
            count = len(__ad_links)))

    def parse_item(self, response):
        """
        """
        # select only the part of the page dedicated to the ad
        # ie discard header, menus etc
        __loader = self._loader_class(
            item=self._item_class(),
            selector=response.xpath(self._ad_xpath))

        __loader.add_value('url', response.url)

        # scrape generic ad attributes
        for __field, __xpath in self._ad_generic_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        # scrape attributes specific to given type of ad (say real-estate)
        for __field, __xpath in self._ad_specific_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        return __loader.load_item()
