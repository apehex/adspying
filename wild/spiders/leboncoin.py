# -*- coding: utf-8 -*-

"""
=========
Leboncoin
=========

Customize the spiders for leboncoin.
"""

from __future__ import division, print_function, absolute_import

import re
from urllib.parse import urlencode, urljoin

import scrapy

from typical import checks

from wild.items import SecondHandAd, SecondHandAdLoader

#####################################################################
# URL TEMPLATE
#####################################################################

BASE_URL = 'https://www.leboncoin.fr/recherche/?'

PRICE_VALUE_TEMPLATE = '{min}-{max}'

#####################################################################
# GENERIC ARGS
#####################################################################

CATEGORY_VALUES = {
    None: '',
    'appliances': '20',
    'caravaning': '4',
    'utility': '5', # utility vehicules
    'networking': '17',
    'real_estate': '9',
    'shoes': '53',
    'sports': '29',
}

LOCATION_VALUES = {
    None: '',
    'rhone_alpes': 'r_22'
}

#####################################################################
# SPIDER
#####################################################################

#####################################################################
# REAL-ESTATE DATA SELECTION
#####################################################################

REALESTATE_AD_ATTRIBUTE_XPATH = {
    'energy': (
        '//div[contains(@data-qa-id, "criteria_item_energy_rate")]'
        + '/div/div[2]/text()'),
    'ges': (
        '//div[contains(@data-qa-id, "criteria_item_ges")]'
        + '/div/div[2]/text()'),
    'rooms': (
        '//div[contains(@data-qa-id, "criteria_item_rooms")]'
        + '/div/div[2]/text()'),
    'square': (
        '//div[contains(@data-qa-id, "criteria_item_square")]'
        + '/div/div[2]/text()'),
    'type': (
        '//div[contains(@data-qa-id, "criteria_item_real_estate_type")]'
        + '/div/div[2]/text()'),}

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = ['www.leboncoin.fr']

    #################################################################
    # AD LISTING DATA SELECTION
    #################################################################
    AD_LISTING_XPATH = (
        '//section[@id="container"]/main/div'
        + '/div[contains(@class,"_3iQ0i")]'
        + '/div[contains(@class,"l17WS")]/div'
        + '/div[contains(@class,"_2Njaz")]'
        + '/div[contains(@class,"_358dQ")]'
        + '/div/div/ul/li')
    AD_LISTING_ATTRIBUTES_XPATH = {
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

    #################################################################
    # AD PAGE DATA SELECTION
    #################################################################
    AD_XPATH = (
        '//section[@id="container"]/main/div/div/div'
        + '/section/section[contains(@class, "_35sFG")]'
        + '/section[contains(@class, "OjX8R")]')
    AD_GENERIC_ATTRIBUTES_XPATH = {
        'images': (
            'div[contains(@class, "_2NKYa")]'
            + '/div[contains(@data-qa-id, "adview_gallery_container")]/div'
            + '/div[contains(@class, "GwNx3")]/div'
            + '/div[contains(@class, "_3bgJP")]/div/div/div'
            + '/div[contains(@class, "_2x8BQ")]/img/@src'),
        'title': (
            'div[contains(@class, "_2NKYa")]'
            + '/div[contains(@class, "_3aOPO")]'
            + '/div[contains(@class, "_14taM")]'
            + '/div[1]/h1/text()'),
        'price': (
            'div[contains(@class, "_2NKYa")]'
            + '/div[contains(@class, "_3aOPO")]'
            + '/div[contains(@class, "_14taM")]'
            + '/div[contains(@class, "eVLNz")]/div/span/text()'),
        'condition': (
            '//div[contains(@data-qa-id, "criteria_item_item_condition")]'
            + '/div/div[2]/text()'),
        'last_updated': (
            'div[contains(@class, "_2NKYa")]'
            + '/div[contains(@class, "_3aOPO")]'
            + '/div[contains(@class, "_14taM")]'
            + '/div[contains(@data-qa-id, "adview_date")]/text()'),
        'location': (
            'div/div/div/div/div[contains(@class, "_1aCZv")]'
            + '/span/text()'),
        'description': (
            'div/div/div/div'
            + '/span[contains(@class, "content-CxPmi")]/text()'),}

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '',
            'locations': '',
            'page': '1',
            'price': '',
            'shippable': '1',
            'text': ''}
        self._urls = [
            BASE_URL, # repeat for each target page
            # BASE_URL, # search page 2
            # BASE_URL, # etc
            # BASE_URL,
        ]

        # 
        self._ad_specific_attributes_xpath = {} # intended to be overriden by the subclass

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader

    def start_requests(self):
        """
        """
        __category = CATEGORY_VALUES.get(
            re.sub(
                '\W+',
                '_',
                getattr(self, 'category', 'real_estate')),
            '9')
        __location = LOCATION_VALUES.get(
            re.sub(
                '\W+',
                '_',
                getattr(self, 'locations', 'rhone_alpes')),
            'r_22')

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
            LeboncoinSpider.AD_LISTING_XPATH).xpath(
            LeboncoinSpider.AD_LISTING_ATTRIBUTES_XPATH['url']).getall()

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
            selector=response.xpath(LeboncoinSpider.AD_XPATH))

        __loader.add_value('url', response.url)

        # scrape generic ad attributes
        for __field, __xpath in LeboncoinSpider.AD_GENERIC_ATTRIBUTES_XPATH.items():
            __loader.add_xpath(__field, __xpath)

        # scrape attributes specific to given type of ad (say real-estate)
        for __field, __xpath in self._ad_specific_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        return __loader.load_item()
