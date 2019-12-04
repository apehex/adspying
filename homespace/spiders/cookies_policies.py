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
            'amazon': 'https://www.amazon.fr/gp/help/customer/display.html/?nodeId=201890250',
            'facebook': 'https://www.facebook.com/policies/cookies/',
            'google': 'https://policies.google.com/technologies/cookies',
            'linkedin': 'https://www.linkedin.com/legal/preview/cookie-policy',
            'stackoverflow': 'https://stackoverflow.com/legal/cookie-policy',
            'wikimedia': 'https://foundation.wikimedia.org/wiki/Cookie_statement',}
