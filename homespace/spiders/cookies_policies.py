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
            'amazon': {
                'url': 'https://www.amazon.fr/gp/help/customer/display.html/?nodeId=201890250',
                'selector': (
                    '//div[contains(@class, "help-content")]')},
            'facebook': {
                'url': 'https://www.facebook.com/policies/cookies/',
                'selector': (
                    '//div[@id="content"]//div[contains(@class, "_5tkp")]')},
            'google': {
                'url': 'https://policies.google.com/technologies/cookies',
                'selector': (
                    '//*[@id="yDmH0d"]//div[contains(@class, "tk9x4e")]'
                    + '/div[contains(@class,"vwhFIf")]')},
            'linkedin': {
                'url': 'https://www.linkedin.com/legal/preview/cookie-policy',
                'selector': '//div[@id="popmain"]//div[contains(@class, "legal-content")]'},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/cookie-policy',
                'selector': (
                    '//div[@id="content"]//main')},
            'wikimedia': {
                'url': 'https://foundation.wikimedia.org/wiki/Cookie_statement',
                'selector': '//div[@id="content"]'},}
