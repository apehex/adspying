# -*- coding: utf-8 -*-

"""
======
Vinted
======

Base class for scraping vinted.

This parent class defines the meta to query vinted over https and
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

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader
from homespace.spiders._secondhandads import SecondHandAdsSpider

#####################################################################
# SPIDER
#####################################################################

class VintedSpider(SecondHandAdsSpider):
    name = 'vinted'
    allowed_domains = ['www.vinted.fr']

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(VintedSpider, self).__init__(*args, **kwargs)

        # stop condition
        self._max_pages = 1
        self._max_age = 1 # in days

        # url template
        self._base_url = 'https://www.vinted.fr/'
        self._search_page_url = '/{category}?{{}}'

        # forge a url to query vinted
        self._current_query_name = 'default'
        self._current_query_args = {}
        self._queries = {
            'default': {
                'category': 'vetements',
                'locations': '',
                'page': '1',
                'price_to': '',
                'search_text': '',
                'size_id[]': '',},
            'chaussures_scarpa_42':{
                'category': 'hommes/chaussures',
                'page': '1',
                'price_to': '100',
                'brand_id[]': '6055',
                'size_id[]': '784',},
            'chaussures_sportiva_42':{
                'category': 'hommes/chaussures',
                'page': '1',
                'price_to': '100',
                'brand_id[]': '201320',
                'size_id[]': '784',},
            'polaire_s':{
                'category': 'vetements',
                'locations': '',
                'page': '1',
                'price_to': '100',
                'search_text': 'mammut',
                'size_id[]': '207',},
            'veste_hardshell_s':{
                'category': 'vetements',
                'locations': '',
                'page': '1',
                'price_to': '200',
                'search_text': 'mammut',
                'size_id[]': '207',},}

        #############################################################
        # AD LISTING DATA SELECTION
        #############################################################
        self._ad_listing_xpath = (
            '//*[@id="catalog"]'
            + '//div[contains(@class, "item-box__container")]')
        self._ad_listing_attributes_xpath = {
            'images': 'section/figure/div/a/img/@src',
            'url': 'section/figure/div/a/@href',}

        #############################################################
        # AD PAGE DATA SELECTION
        #############################################################
        self._ad_xpath = '//main[contains(@class, "item-information")]'
        self._ad_generic_attributes_xpath = {
            'images': (
                '//div[contains(@class, "item-photos")]'
                + '//figure[contains(@class, "item-photo--1")]/a/@href'),
            'title': '//div[contains(@itemprop, "name")]/span/text()',
            'price': '//span[contains(@itemprop, "price")]/div/text()',
            'condition': '//div[contains(@itemprop, "itemCondition")]/text()',
            'last_updated': '//time/@datetime',
            'location': '//div[contains(@class, "details-list--country")]/text()',
            'description': '//div[contains(@itemprop, "description")]/span/text()',}

        # select data specific to a given ad search (say smartphones)
        self._ad_specific_attributes_xpath = {} # intended to be overriden by the subclass

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader

    def start_requests(self):
        """
        """
        self._select_current_query()
        self._search_page_url = self._search_page_url.format(
            category=self._current_query_args.get(
                'category',
                'hommes'))

        return super(VintedSpider, self).start_requests()
