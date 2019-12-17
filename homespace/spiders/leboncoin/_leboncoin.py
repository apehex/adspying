# -*- coding: utf-8 -*-

"""
=========
Leboncoin
=========

Base class for scraping leboncoin.

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

from homespace.items._secondhandad import SecondHandAd, SecondHandAdLoader
from homespace.spiders._secondhandads import SecondHandAdsSpider

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSpider(SecondHandAdsSpider):
    name = 'leboncoin'
    allowed_domains = ['www.leboncoin.fr']

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSpider, self).__init__(*args, **kwargs)

        # stop condition
        self._max_pages = 1
        self._max_age = 1 # in days

        # url template
        self._base_url = 'https://www.leboncoin.fr/'
        self._search_page_url = '/recherche/?{}'

        # forge a url to query leboncoin
        self._current_query_name = 'default'
        self._current_query_args = {}
        self._queries = {
            'default': {
                'category': '',
                'locations': '',
                'page': '1',
                'price': '',
                'search_in': '',
                'shippable': '1',
                'text': ''}}

        #############################################################
        # AD LISTING DATA SELECTION
        #############################################################
        self._ad_listing_xpath = (
            '//section[@id="container"]'
            + '//li[contains(@data-qa-id, "aditem_container")]')
        self._ad_listing_attributes_xpath = {
            'images': (
                'a/div/span[contains(@class, "_a3cT")]'
                + '/div/img/@src'),
            'title': 'a/@title',
            'price': (
                'a/section[contains(@class, "_2EDA9")]/div/div/span'
                + '/span[contains(@class, "_1NfL7")]/text()'),
            'location': (
                'a/section[contains(@class, "_2EDA9")]/div'
                + '/p[contains(@class,"_2qeuk")]/text()'),
            'last_updated': (
                'a/section[contains(@class, "_2EDA9")]/div'
                + '/p[contains(@class,"mAnae")]/text()'),
            'url': 'a/@href',}


        #############################################################
        # AD PAGE DATA SELECTION
        #############################################################
        self._ad_xpath = (
            '//section[@id="container"]/main/div/div/div'
            + '/section/section[contains(@class, "_35sFG")]'
            + '/section[contains(@class, "OjX8R")]')
        self._ad_generic_attributes_xpath = {
            'images': (
                'div[contains(@class, "_2NKYa")]'
                + '/div[contains(@data-qa-id, "adview_gallery_container")]/div'
                + '/div[contains(@class, "GwNx3")]/div'
                + '/div[contains(@class, "_3bgJP")]/div/div/div'
                + '/div[contains(@class, "_2x8BQ")]/img/@src'),
            'title': '//div[contains(@data-qa-id, "adview_title")]/h1/text()',
            'price': (
                '//div[contains(@data-qa-id, "adview_price")]'
                + '/div/span/text()'),
            'condition': (
                '//div[contains(@data-qa-id, "criteria_item_item_condition")]'
                + '/div/div[2]/text()'),
            'last_updated': (
                '//div[contains(@data-qa-id, "adview_date")]/text()'),
            'location': (
                '//div[contains(@data-qa-id, "adview_location_informations")]'
                + '/span/text()'),
            'description': (
                '//div[contains(@data-qa-id, "adview_description_container")]'
                + '//span[contains(@class, "content-CxPmi")]/text()'),}

        # select data specific to a given ad search (say smartphones)
        self._ad_specific_attributes_xpath = {} # intended to be overriden by the subclass

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader
