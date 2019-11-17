# -*- coding: utf-8 -*-

"""
======
Amazon
======

Base class for scraping amazon.

The scraped data is compiled into a referential to complete the information
written in the 

This parent class defines the meta to query leboncoin over https and
actually performs the processing.

Every child class customize the meta to fit a specific ad search:
- query args
- data selectors
- ad attributes

For example, an appliance ad will specify the "condition" of the 
item while a real-estate ad has no use for such an attribute.

But all ads are layed out in a similar way, in HTML.
"""

from __future__ import division, print_function, absolute_import

import re
from urllib.parse import urlencode, urljoin

import scrapy

from typical import checks

from homespace.cli import remove_special_characters
from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# URL TEMPLATE
#####################################################################

BASE_URL = 'https://www.amazon.fr/s?'
'i=electronics'
'&bbn=218193031'
'&rh=n:13921051,n:%2113910671,n:14060661,n:218193031'
'&field-feature_keywords_two_browse-bin=2503729031'
'&pf_rd_i=218193031'
'&pf_rd_m=A1X6FK5RDHNB96'
'&pf_rd_p=c49a2c0f-0b56-4353-987d-36ef51a8f344'
'&pf_rd_r=KVDRJGNGRG03J51K532A'
'&pf_rd_s=merchandised-search-2'
'&pf_rd_t=101'
'&ref=s9_acsd_dnav_bw_ct_x_ct01'
'https://www.amazon.fr/s?k=huawei+p8+lite&i=electronics&rh=n:13921051,n:218193031,p_76:437878031'

PRICE_VALUE_TEMPLATE = '{min}-{max}'

#####################################################################
# GENERIC ARGS
#####################################################################

CATEGORY_VALUES = {}

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.fr']

    #################################################################
    # ITEM LISTING DATA SELECTION
    #################################################################
    ITEM_LISTING_XPATH = ''
    ITEM_LISTING_ATTRIBUTES_XPATH = {
        'images': '',
        'title': '',
        'price': '',
        'location': '',
        'last_updated': '',
        'url': '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a',}

    #################################################################
    # ITEM PAGE DATA SELECTION
    #################################################################
    ITEM_XPATH = ''
    ITEM_GENERIC_ATTRIBUTES_XPATH = {
        'images': '',
        'title': '',
        'price': '',
        'condition': '',
        'last_updated': '',
        'location': '',
        'description': '',}

    #################################################################
    # CLI
    #################################################################

    def _parse_cli_args(
            self):
        """
        Clean, format and translate to match the leboncoin url referential.
        """
        for __key, __value in self._search_args.items():
            self._search_args[__key] = getattr(
                self,
                __key,
                __value) # default to the current value

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'i': 'electronics',
                'k': 'huawei',
                'rh': 'n:218193031',
                'page': ''}}
        self._urls = [
            BASE_URL, # repeat for each target page
            # BASE_URL, # search page 2
            # BASE_URL, # etc
            # BASE_URL,
        ]

        # select data specific to a given ad search (say smartphones)
        self._ad_specific_attributes_xpath = {} # intended to be overriden by the subclass

        # classes to store, clean and export the data
        self._item_class = SecondHandItem
        self._loader_class = SecondHandItemLoader

    def start_requests(self):
        """
        """
        # translate the cli args to the url std for leboncoin
        self._parse_cli_args()

        # forge the search urls & queue the requests
        for i, __url in enumerate(self._urls):
            self._search_args['page'] = str(i + 1)
            yield scrapy.Request(
                url=__url + urlencode(self._search_args),
                callback=self.parse_listing)

    def parse_listing(self, response):
        """
        """
        __page = re.match(r'.*page=(\d{1,2}).*', response.url).group(1)
        __ad_links = response.xpath(
            LeboncoinSpider.ITEM_LISTING_XPATH).xpath(
            LeboncoinSpider.ITEM_LISTING_ATTRIBUTES_XPATH['url']).getall()

        for __link in __ad_links:
            yield scrapy.Request(
                url=urljoin('https://www.leboncoin.fr/', __link),
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
            selector=response.xpath(LeboncoinSpider.ITEM_XPATH))

        __loader.add_value('url', response.url)

        # scrape generic ad attributes
        for __field, __xpath in LeboncoinSpider.ITEM_GENERIC_ATTRIBUTES_XPATH.items():
            __loader.add_xpath(__field, __xpath)

        # scrape attributes specific to given type of ad (say real-estate)
        for __field, __xpath in self._ad_specific_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        return __loader.load_item()
