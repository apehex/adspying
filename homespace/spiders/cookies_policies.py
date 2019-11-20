# -*- coding: utf-8 -*-

"""
==============
Cookies Policy
==============

Scrape and version the cookies policies of web providers.

Cookies have some important implications on the privacy and anonymity
of web users. Web providers are expected to state the use they make of
cookies.
"""

from __future__ import division, print_function, absolute_import

import scrapy

from typical import checks

from homespace.items._legaldocument import LegalDocument, LegalDocumentLoader

#####################################################################
# SPIDER
#####################################################################

class CookiesPoliciesSpider(scrapy.Spider):
    name = 'cookies_policies'

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(
            self,
            *args,
            **kwargs):
        """
        Initiate the scraping env.
        """
        super(CookiesPoliciesSpider, self).__init__(*args, **kwargs)

        # enable specific pipelines
        self._pipelines = ['LegalDocumentPipeline']

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'google': {
                'url': 'https://policies.google.com/technologies/cookies',
                'selector': (
                    '//*[@id="yDmH0d"]/c-wiz/div/div'
                    + '/div[contains(@class, "tk9x4e")]'
                    + '/div[contains(@class,"vwhFIf")]/text()')},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/cookie-policy',
                'selector': (
                    '//*[@id="content"]/div/div'
                    + '/div[contains(@class, "grid--cell9")]'
                    + '/main/text()')},
            'amazon': {
                'url': 'https://www.amazon.fr/gp/help/customer/display.html/?nodeId=201890250',
                'selector': (
                    '/body/div[contains(@class, "cs-help-v4")]'
                    + '/div[contains(@class, "cs-help-container")]'
                    + '/div[contains(@class, "cs-help-content")]'
                    + '/div[1]/div[contains(@class, "help-content")]/text()')},
            'wikimedia': {
                'url': 'https://foundation.wikimedia.org/wiki/Cookie_statement',
                'selector': '//*[@id="content"]/text()'},
            'facebook': {
                'url': 'https://www.facebook.com/policies/cookies/',
                'selector': (
                    '//*[@id="content"]/div/div/div'
                    + '/div[contains(@class, "_5tkp")]/text()')}}

    def start_requests(
            self):
        """
        Queue all the legal document's urls.
        """
        # forge the search urls & queue the requests
        for __provider, __meta in self.providers.items():
            self.log('[{provider}] requesting cookies policy...'.format(
                provider=__provider))
            yield scrapy.Request(
                url=__meta['url'],
                callback=self.parse,
                meta={'provider': __provider, 'selector': __meta['selector']})

    def parse(
            self,
            response):
        """
        Process the downloaded html pages.
        """
        __provider = response.meta.get(
            'provider',
            'none')
        __selector = response.meta.get(
            'selector',
            '//body')

        self.log('[{provider}] parsing cookies policy...'.format(
            provider = __provider))

        __loader = LegalDocumentLoader(
            item=LegalDocument(),
            response=response)

        __loader.add_value('url', response.url)
        __loader.add_value('provider', __provider)
        __loader.add_xpath('text', __selector)

        return __loader.load_item()
