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
            'amazon': 'https://www.amazon.fr/gp/help/customer/display.html?nodeId=201909010',
            'edf': 'https://particulier.edf.fr/fr/accueil/cookies-et-donnees-personnelles/charte-donnees-personnelles.html',
            'steam': 'https://store.steampowered.com/privacy_agreement/',
            'auvieuxcampeur': 'https://www.auvieuxcampeur.fr/reglement-vie-privee',
            'github': 'https://help.github.com/articles/github-privacy-statement/',
            'linkedin': 'https://www.linkedin.com/legal/preview/privacy-policy',
            'pivotal': 'https://pivotal.io/privacy-policy',
            'steam': 'https://store.steampowered.com/privacy_agreement/',
            'auvieuxcampeur': 'https://www.auvieuxcampeur.fr/reglement-vie-privee',
            'couchsurfing': 'https://www.couchsurfing.com/about/privacy-policy/',
            'medium': 'https://medium.com/policy/medium-privacy-policy-f03bf92035c9',
            'stackoverflow': 'https://stackoverflow.com/legal/privacy-policy',
            'clickworker': 'https://workplace.clickworker.com/en/agreements/10124?_ga=2.126543375.300522425.1531068679-588812912.1531068679',
            'slack': 'https://slack.com/intl/fr-fr/policy-archives/privacy/2014-07-22',
            'uber': 'https://privacy.uber.com/policy',
            'google': 'https://policies.google.com/privacy?hl=en&gl=zz',
            'mbefrance': 'https://www.mbefrance.fr/fr/politique-confidentialite',
            'pornhub': 'https://fr.pornhub.com/information',
            'xhamster': 'https://fr.xhamster.com/info/privacy',
            'trustpilot': 'https://legal.trustpilot.com/end-user-privacy-terms',
            'wikimedia': 'https://foundation.wikimedia.org/wiki/Privacy_policy',
            'reddit': 'https://www.redditinc.com/policies/privacy-policy',
            'homebox': 'https://www.homebox.fr/politique-de-protection-des-donnees-personnelles',
            'hardloop': 'https://www.hardloop.fr/infos/protection-des-donnees',
            'kaggle': 'https://www.kaggle.com/privacy',
            'codingame': 'https://www.codingame.com/legal/privacy-policy',
            'winamax': 'https://www.winamax.fr/a-propos_conditions-generales-d-utilisation_politique-de-confidentialite',
            'mozilla': 'https://www.mozilla.org/en-US/privacy/',
            'bluely': 'https://www.bluely.eu/en/gestion-donnees-personnelles',
            'facebook': 'https://www.facebook.com/privacy/explanation',
            'microsoft': 'https://privacy.microsoft.com/en-US/privacystatement',}
