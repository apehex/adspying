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

class ServiceTermsSpider(LegalDocumentsSpider):
    name = 'service_terms'

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
        super(ServiceTermsSpider, self).__init__(*args, **kwargs)

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'auvieuxcampeur': {
                'url': 'https://www.auvieuxcampeur.fr/mention-legale',
                'selector': ''},
            'bluely': {
                'url': 'https://www.bluely.eu/en/legal-notices',
                'selector': ''},
            'clickworker': {
                'url': 'https://workplace.clickworker.com/en/agreements/10123?_ga=2.234456860.300522425.1531068679-588812912.1531068679',
                'selector': ''},
            'github': {
                'url': 'https://help.github.com/articles/github-terms-of-service/',
                'selector': ''},
            'google': {
                'url': 'https://policies.google.com/terms?hl=en&gl=zz',
                'selector': ''},
            'homebox': {
                'url': 'https://www.homebox.fr/mentions-legales',
                'selector': ''},
            'hardloop': {
                'url': 'https://www.hardloop.fr/infos/cgu',
                'selector': ''},
            'kaggle': {
                'url': 'https://www.kaggle.com/terms',
                'selector': ''},
            'medium': {
                'url': 'https://medium.com/policy/medium-terms-of-service-9db0094a1e0f',
                'selector': ''},
            'microsoft': {
                'url': 'https://www.microsoft.com/en/servicesagreement/',
                'selector': ''},
            'pivotal': {
                'url': 'https://pivotal.io/svcs-terms',
                'selector': ''},
            'pornhub': {
                'url': 'https://fr.pornhub.com/information',
                'selector': ''},
            'redditinc': {
                'url': 'https://www.redditinc.com/policies/content-policy',
                'selector': ''},
            'slack': {
                'url': 'https://slack.com/intl/fr-fr/policy-archives/terms-of-service-user/2016-11-17',
                'selector': ''},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/terms-of-service/public',
                'selector': ''},
            'trustpilot': {
                'url': 'https://legal.trustpilot.com/end-user-terms-and-conditions',
                'selector': ''},
            'xhamster': {
                'url': 'https://fr.xhamster.com/info/terms',
                'selector': ''},}
