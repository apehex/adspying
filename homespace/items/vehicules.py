# -*- coding: utf-8 -*-

"""
============
Vehicule Ads
============

Items scraped from vehicule ads.
"""

from __future__ import division, print_function, absolute_import

from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VehiculeAd(SecondHandAd):
    """
    """
    # Specifications
    fuel = Field()
    mileage = Field()
    consumption = Field()
    size_inside = Field()
    size_outside = Field()
    gearbox = Field()

class VehiculeAdLoader(SecondHandAdLoader):
    """
    """
    # Specifications
    fuel_in = Join()
    fuel_out = Identity()

    mileage_in = Join()
    mileage_out = Identity()

    consumption_in = Join()
    consumption_out = Identity()

    size_inside_in = Join()
    size_inside_out = Identity()

    size_outside_in = Join()
    size_outside_out = Identity()

    gearbox_in = Join()
    gearbox_out = Identity()
