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
                'selector': '//*[@id="maincontent"]'},
            'bluely': {
                'url': 'https://www.bluely.eu/en/legal-notices',
                'selector': (
                    '//*[@id="main-content"]/main/div/div/div'
                    + '/div[contains(@class, "content-base")]')},
            'clickworker': {
                'url': 'https://workplace.clickworker.com/en/agreements/10123?_ga=2.234456860.300522425.1531068679-588812912.1531068679',
                'selector': '//*[@id="agreements"]'},
            'github': {
                'url': 'https://help.github.com/articles/github-terms-of-service/',
                'selector': '//main/main/article'},
            'google': {
                'url': 'https://policies.google.com/terms',
                'selector': (
                    '//*[@id="yDmH0d"]/c-wiz/div/div/div[2]/div[3]/c-wiz/div'
                    +' /div[contains(@class, "nrAB0c")]')},
            'homebox': {
                'url': 'https://www.homebox.fr/mentions-legales',
                'selector': (
                    '/html/body/div[4]/div/div[2]/section'
                    + '/div[contains(@class, "region"])')},
            'hardloop': {
                'url': 'https://www.hardloop.fr/infos/cgu',
                'selector': (
                    '//*[@id="root"]/div'
                    + '/div[contains(@class, "mainContent")]'
                    + '/div[contains(@class, "InfoShowBannerWrapper")]'
                    + '/div/div/div')},
            'kaggle': {
                'url': 'https://www.kaggle.com/terms',
                'selector': (
                    '/html/body/main/div'
                    + '/div[contains(@class, "main-content")]/div/div/div')},
            'medium': {
                'url': 'https://medium.com/policy/medium-terms-of-service-9db0094a1e0f',
                'selector': '//*[@id="root"]/div/article/div/section'},
            'microsoft': {
                'url': 'https://www.microsoft.com/en/servicesagreement/',
                'selector': '//div[contains(@class, "div_content")]'},
            'pivotal': {
                'url': 'https://pivotal.io/svcs-terms',
                'selector': (
                    '//*[@id="viewport"]/div'
                    + '/div[contains(@class, "content")]')},
            'pornhub': {
                'url': 'https://fr.pornhub.com/information#terms',
                'selector': '//*[@id="information_terms"]'},
            'redditinc': {
                'url': 'https://www.redditinc.com/policies/user-agreement',
                'selector': '//*[@id="content"]'},
            'slack': {
                'url': 'https://slack.com/intl/en-fr/terms-of-service',
                'selector': (
                    '//*[@id="main"]/div/div/div'
                    + '/div[contains(@class, "legal-content")]')},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/terms-of-service/public',
                'selector': '//*[@id="content"]/div/div/div[2]/main'},
            'trustpilot': {
                'url': 'https://legal.trustpilot.com/end-user-terms-and-conditions',
                'selector': (
                    '/html/body'
                    + '/div[contains(@class, "content")]/main')},
            'xhamster': {
                'url': 'https://fr.xhamster.com/info/terms',
                'selector': (
                    '/html/body'
                    + '/div[contains(@class, "main-wrap")]'
                    + '/div/main/article')},}
