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
from scrapy.loader import ItemLoader

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

PRICE_VALUES = {
    None: [],
    'appliances': (
        [0, 5]
        + list(range(10, 50, 10))
        + list(range(50, 100, 25))
        + list(range(100, 550, 100))),
    'caravaning': (
        list(range(0, 1000, 250))
        + list(range(1000, 3000, 500))
        + list(range(3000, 15000, 1000))
        + list(range(15000, 30000, 2500))
        + list(range(30000, 55000, 5000))),
    'networking': (
        [0, 5]
        + list(range(10, 50, 10))
        + list(range(50, 100, 25))
        + list(range(100, 550, 100))),
    'real_estate': [],
    'shoes': [],
    'sports': [],
}

#####################################################################
# VEHICULE ARGS
#####################################################################

URL_ARGS = {
    'result_page_number': 'o',
    'min_year': 'rs',
    'max_year': 're',
    'min_price': 'price=min-',
    'max_price': 'pe',
    'min_mileage': 'ms',
    'max_mileage': 'me',
    'fuel_type': 'fu'}

FUEL_ARG = {
    'petrol': 1,
    'diesel': 2,
    'lpg': 3,
    'electric': 4,
    'hybrid': 5}

#####################################################################
# GENERIC DATA SELECTION
#####################################################################

LISTING_ITEM_XPATH = (
    '//section[@id="container"]/main/div'
    + '/div[contains(@class,"_3iQ0i")]'
    + '/div[contains(@class,"l17WS")]/div'
    + '/div[contains(@class,"_2Njaz")]'
    + '/div[contains(@class,"_358dQ")]'
    + '/div/div/ul/li')
LISTING_ITEM_ATTRIBUTE_XPATH = {
    'image': 'a/div/span[contains(@class, "_a3cT")]/div/img/@src',
    'title': 'a/@title',
    'price': 'a/section[contains(@class, "_2EDA9")]/div/div/span/span[contains(@class, "_1NfL7")]/text()',
    'location': 'a/section[contains(@class, "_2EDA9")]/div/p[contains(@class,"_2qeuk")]/text()',
    'last_updated': 'a/section[contains(@class, "_2EDA9")]/div/p[contains(@class,"mAnae")]/text()',
    'url': 'a/@href',}

ITEM_AD_XPATH = (
    '//section[@id="container"]/main/div/div/div'
    + '/section/section[contains(@class, "_35sFG")]'
    + '/section[contains(@class, "OjX8R")]')
ITEM_AD_ATTRIBUTE_XPATH = {
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

SHOE_AD_ATTRIBUTE_XPATH = {
    'category': (
        '//div[contains(@data-qa-id, "criteria_item_shoe_category")]'
        + '/div/div[2]/text()'),
    'color': (
        '//div[contains(@data-qa-id, "criteria_item_clothing_color")]'
        + '/div/div[2]/text()'),
    'size': (
        '//div[contains(@data-qa-id, "criteria_item_shoe_size")]'
        + '/div/div[2]/text()'),
    'type': (
        '//div[contains(@data-qa-id, "criteria_item_shoe_type")]'
        + '/div/div[2]/text()'),}

#####################################################################
# STRIP IRRELEVANT CHARS
#####################################################################

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = ['www.leboncoin.fr']

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

        __urls = [
            BASE_URL, # repeat for each target page
            # BASE_URL, # search page 2
            # BASE_URL, # etc
            # BASE_URL,
        ]
        __args = {
            'page': '1',
            'shippable': '1',
            'category': __category,
            'locations': __location,
            'text': getattr(self, 'query', '')}

        for i, __url in enumerate(__urls):
            __args['page'] = str(i + 1)
            yield scrapy.Request(
                url=__url + urlencode(__args),
                callback=self.parse_listing)

    def parse_listing(self, response):
        """
        """
        __page = re.match(r'.*page=(\d{1,2}).*', response.url).group(1)
        __item_links = response.xpath(LISTING_ITEM_XPATH).xpath(LISTING_ITEM_ATTRIBUTE_XPATH['url']).getall()

        for __link in __item_links:
            yield scrapy.Request(
                url=urljoin('https://www.leboncoin.fr/', __link),
                callback=self.parse_item)

        self.log('[Page {page}] {count} ads queued...'.format(
            page = __page,
            count = len(__item_links)))

    def parse_item(self, response):
        """
        """
        __loader = SecondHandAdLoader(
            item=SecondHandAd(),
            selector=response.xpath(ITEM_AD_XPATH))

        __loader.add_value('url', response.url)
        __loader.add_xpath('title', ITEM_AD_ATTRIBUTE_XPATH['title'])
        __loader.add_xpath('price', ITEM_AD_ATTRIBUTE_XPATH['price'])
        __loader.add_xpath('location', ITEM_AD_ATTRIBUTE_XPATH['location'])
        __loader.add_xpath('last_updated', ITEM_AD_ATTRIBUTE_XPATH['last_updated'])
        __loader.add_xpath('description', ITEM_AD_ATTRIBUTE_XPATH['description'])

        return __loader.load_item()
