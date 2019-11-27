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

class PrivacyPoliciesSpider(LegalDocumentsSpider):
    name = 'privacy_policies'

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
        super(PrivacyPoliciesSpider, self).__init__(*args, **kwargs)

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'amazon': {
                'url': 'https://www.amazon.fr/gp/help/customer/display.html?nodeId=201909010',
                'selector': ''},
            'edf': {
                'url': 'https://particulier.edf.fr/fr/accueil/cookies-et-donnees-personnelles/charte-donnees-personnelles.html',
                'selector': ''},
            'steam': {
                'url': 'https://store.steampowered.com/privacy_agreement/',
                'selector': ''},
            'auvieuxcampeur': {
                'url': 'https://www.auvieuxcampeur.fr/reglement-vie-privee',
                'selector': '',
                'language': 'fr'},
            'github': {
                'url': 'https://help.github.com/articles/github-privacy-statement/',
                'selector': ''},
            'linkedin': {
                'url': 'https://www.linkedin.com/legal/preview/privacy-policy',
                'selector': '//*[@id="popmain"]/div[contains(@class, "legal-content")]'},
            'pivotal': {
                'url': 'https://pivotal.io/privacy-policy',
                'selector': ''},
            'steam': {
                'url': 'https://store.steampowered.com/privacy_agreement/',
                'selector': ''},
            'auvieuxcampeur': {
                'url': 'https://www.auvieuxcampeur.fr/reglement-vie-privee',
                'selector': ''},
            'couchsurfing': {
                'url': 'https://www.couchsurfing.com/about/privacy-policy/',
                'selector': ''},
            'medium': {
                'url': 'https://medium.com/policy/medium-privacy-policy-f03bf92035c9',
                'selector': ''},
            'stackoverflow': {
                'url': 'https://stackoverflow.com/legal/privacy-policy',
                'selector': ''},
            'clickworker': {
                'url': 'https://workplace.clickworker.com/en/agreements/10124?_ga=2.126543375.300522425.1531068679-588812912.1531068679',
                'selector': ''},
            'slack': {
                'url': 'https://slack.com/intl/fr-fr/policy-archives/privacy/2014-07-22',
                'selector': ''},
            'uber': {
                'url': 'https://privacy.uber.com/policy',
                'selector': ''},
            'google': {
                'url': 'https://policies.google.com/privacy?hl=en&gl=zz',
                'selector': ''},
            'mbefrance': {
                'url': 'https://www.mbefrance.fr/fr/politique-confidentialite',
                'selector': ''},
            'pornhub': {
                'url': 'https://fr.pornhub.com/information',
                'selector': ''},
            'xhamster': {
                'url': 'https://fr.xhamster.com/info/privacy',
                'selector': ''},
            'trustpilot': {
                'url': 'https://legal.trustpilot.com/end-user-privacy-terms',
                'selector': ''},
            'wikimedia': {
                'url': 'https://foundation.wikimedia.org/wiki/Privacy_policy',
                'selector': ''},
            'reddit': {
                'url': 'https://www.redditinc.com/policies/privacy-policy',
                'selector': ''},
            'homebox': {
                'url': 'https://www.homebox.fr/politique-de-protection-des-donnees-personnelles',
                'selector': ''},
            'hardloop': {
                'url': 'https://www.hardloop.fr/infos/protection-des-donnees',
                'selector': ''},
            'kaggle': {
                'url': 'https://www.kaggle.com/privacy',
                'selector': ''},
            'codingame': {
                'url': 'https://www.codingame.com/legal/privacy-policy',
                'selector': ''},
            'winamax': {
                'url': 'https://www.winamax.fr/a-propos_conditions-generales-d-utilisation_politique-de-confidentialite',
                'selector': ''},
            'mozilla': {
                'url': 'https://www.mozilla.org/en-US/privacy/',
                'selector': ''},
            'bluely': {
                'url': 'https://www.bluely.eu/en/gestion-donnees-personnelles',
                'selector': ''},
            'facebook': {
                'url': 'https://www.facebook.com/privacy/explanation',
                'selector': ''},
            'microsoft': {
                'url': 'https://privacy.microsoft.com/en-US/privacystatement',
                'selector': ''},}
