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

from homespace.spiders._legaldocuments import LegalDocumentsSpider

#####################################################################
# SPIDER
#####################################################################

class CookiesPoliciesSpider(LegalDocumentsSpider):
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

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'google': {
                'url': 'https://policies.google.com/technologies/cookies',
                'selector': (
                    '//*[@id="yDmH0d"]/c-wiz/div/div'
                    + '/div[contains(@class, "tk9x4e")]'
                    + '/div[contains(@class,"vwhFIf")]')},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/cookie-policy',
                'selector': (
                    '//*[@id="content"]/div/div'
                    + '/div[contains(@class, "grid--cell9")]'
                    + '/main')},
            'amazon': {
                'url': 'https://www.amazon.fr/gp/help/customer/display.html/?nodeId=201890250',
                'selector': (
                    '/body/div[contains(@class, "cs-help-v4")]'
                    + '/div[contains(@class, "cs-help-container")]'
                    + '/div[contains(@class, "cs-help-content")]'
                    + '/div[1]/div[contains(@class, "help-content")]')},
            'wikimedia': {
                'url': 'https://foundation.wikimedia.org/wiki/Cookie_statement',
                'selector': '//*[@id="content"]'},
            'facebook': {
                'url': 'https://www.facebook.com/policies/cookies/',
                'selector': (
                    '//*[@id="content"]/div/div/div'
                    + '/div[contains(@class, "_5tkp")]')}}
