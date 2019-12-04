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
            'auvieuxcampeur': 'https://www.auvieuxcampeur.fr/mention-legale',
            'bluely': 'https://www.bluely.eu/en/legal-notices',
            'clickworker': 'https://workplace.clickworker.com/en/agreements/10123?_ga=2.234456860.300522425.1531068679-588812912.1531068679',
            'github': 'https://help.github.com/articles/github-terms-of-service/',
            'google': 'https://policies.google.com/terms',
            'homebox': 'https://www.homebox.fr/mentions-legales',
            'hardloop': 'https://www.hardloop.fr/infos/cgu',
            'kaggle': 'https://www.kaggle.com/terms',
            'linkedin': 'https://www.linkedin.com/legal/preview/user-agreement',
            'medium': 'https://medium.com/policy/medium-terms-of-service-9db0094a1e0f',
            'microsoft': 'https://www.microsoft.com/en/servicesagreement/',
            'pivotal': 'https://pivotal.io/svcs-terms',
            'pornhub': 'https://fr.pornhub.com/information#terms',
            'redditinc': 'https://www.redditinc.com/policies/user-agreement',
            'slack': 'https://slack.com/intl/en-fr/terms-of-service',
            'stackoverflow': 'https://stackoverflow.com/legal/terms-of-service/public'
            'trustpilot': 'https://legal.trustpilot.com/end-user-terms-and-conditions',
            'xhamster': 'https://fr.xhamster.com/info/terms',}
