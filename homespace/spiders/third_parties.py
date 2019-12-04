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

class ThirdPartiesSpider(LegalDocumentsSpider):
    name = 'third_parties'

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
        super(ThirdPartiesSpider, self).__init__(*args, **kwargs)

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'amazon': 'https://www.amazon.fr/gp/help/customer/display.html?nodeId=GDDFZHDDGWM46YS3',
            'google': 'https://policies.google.com/privacy/google-partners?hl=en&gl=zz',
            'paypal': 'https://www.paypal.com/ie/webapps/mpp/ua/third-parties-list',
            'github': 'https://help.github.com/articles/github-subprocessors-and-cookies/',
            'twitter': 'https://gdpr.twitter.com/en/dpa.html'}
