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
            'airbnb': 'https://www.airbnb.com/terms/privacy_policy',
            'amazon': 'https://www.amazon.fr/gp/help/customer/display.html?nodeId=201909010',
            'auvieuxcampeur': 'https://www.auvieuxcampeur.fr/reglement-vie-privee',
            'bluely': 'https://www.bluely.eu/en/gestion-donnees-personnelles',
            'clickworker': 'https://workplace.clickworker.com/en/agreements/10124',
            'couchsurfing': 'https://www.couchsurfing.com/about/privacy-policy/',
            'coursera': 'https://www.coursera.org/about/privacy',
            'codingame': 'https://www.codingame.com/legal/privacy-policy',
            'edf': 'https://particulier.edf.fr/fr/accueil/cookies-et-donnees-personnelles/charte-donnees-personnelles.html',
            'facebook': 'https://www.facebook.com/privacy/explanation',
            'github': 'https://help.github.com/articles/github-privacy-statement/',
            'google': 'https://policies.google.com/privacy?hl=en&gl=zz',
            'hardloop': 'https://www.hardloop.fr/infos/protection-des-donnees',
            'homebox': 'https://www.homebox.fr/politique-de-protection-des-donnees-personnelles',
            'kaggle': 'https://www.kaggle.com/privacy',
            'linkedin': 'https://www.linkedin.com/legal/preview/privacy-policy',
            'mbefrance': 'https://www.mbefrance.fr/fr/politique-confidentialite',
            'medium': 'https://medium.com/policy/medium-privacy-policy-f03bf92035c9',
            'microsoft': 'https://privacy.microsoft.com/en-US/privacystatement',
            'mozilla': 'https://www.mozilla.org/en-US/privacy/',
            'patreon': 'https://privacy.patreon.com/policies',
            'pivotal': 'https://pivotal.io/privacy-policy',
            'pornhub': 'https://fr.pornhub.com/information',
            'reddit': 'https://www.redditinc.com/policies/privacy-policy',
            'slack': 'https://slack.com/intl/fr-fr/policy-archives/privacy/2014-07-22',
            'soundcloud': 'https://soundcloud.com/pages/privacy/',
            'stackoverflow': 'https://stackoverflow.com/legal/privacy-policy',
            'steam': 'https://store.steampowered.com/privacy_agreement/',
            'trustpilot': 'https://legal.trustpilot.com/end-user-privacy-terms',
            'twitter': 'https://twitter.com/en/privacy',
            'uber': 'https://privacy.uber.com/policy',
            'vporn': 'https://www.vporn.com/privacy/',
            'wikimedia': 'https://foundation.wikimedia.org/wiki/Privacy_policy',
            'winamax': 'https://www.winamax.fr/a-propos_conditions-generales-d-utilisation_politique-de-confidentialite',
            'xhamster': 'https://fr.xhamster.com/info/privacy',}
