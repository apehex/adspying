#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tools to assess the fuel consumption."""

from __future__ import absolute_import, division, print_function

################################################################################
# CONSTANTS
################################################################################

US_GALLON = 3.785412	# l
IMP_GALLON = 4.54609	# l
MILE = 1.609344	# km

PETROL_COST = 1.56  # €/l
DIESEL_COST = 1.52  # €/l
ELECTRICITY_COST = 0.15	# €/kWh

###############################################################################
# FUEL EFFICIENCY
###############################################################################

def us_mpg_to_lpkm(mpg):
	"""Convert US mpg to l/100km fuel consumption.

	Args:
		mpg (float): the fuel consumption in miles per US gallon.

	Returns:
		float: the fuel consumption in liters per 100 kilometers.
	"""
	liters_per_hundred_kilometers = 100.0 * US_GALLON / MILE
	if mpg > 0.0:
		liters_per_hundred_kilometers = liters_per_hundred_kilometers / mpg
	else:
		liters_per_hundred_kilometers = 0.0
	return liters_per_hundred_kilometers

def imp_mpg_to_lpkm(mpg):
	"""Convert Imp mpg to l/100km fuel consumption.

	Args:
		mpg (float): the fuel consumption in miles per Imp gallon.

	Returns:
		float: the fuel consumption in liters per 100 kilometers.
	"""
	liters_per_hundred_kilometers = 100.0 * IMP_GALLON / MILE
	if mpg > 0.0:
		liters_per_hundred_kilometers = liters_per_hundred_kilometers / mpg
	else:
		liters_per_hundred_kilometers = 0.0
	return liters_per_hundred_kilometers
	

def lpkm_to_us_mpg(lpkm):
	"""Convert l/100km to US mpg fuel consumption.

	Args:
		lpkm (float): the fuel consumption in liters per 100 kilometers.

	Returns:
		float: the fuel consumption in miles per US gallon.
	"""
	return us_mpg_to_lpkm(lpkm)

def lpkm_to_imp_mpg(lpkm):
	"""Convert l/100km to Imp mpg fuel consumption.

	Args:
		lpkm (float): the fuel consumption in liters per 100 kilometers.

	Returns:
		float: the fuel consumption in miles per Imp gallon.
	"""
	return imp_mpg_to_lpkm(lpkm)

###############################################################################
# ESTIMATION
###############################################################################

def estimate_consumption_to_emission_regression_factor():
	import matplotlib.pyplot as plt
	import pandas as pd

	df = pd.read_csv('van-data.csv')

	pass

def estimate_consumption_from_emission(co2_emission, fuel_type='diesel'):
    """Estimate the fuel consumption according to a given rate of CO2 emission.

    Args:
        co2_emission (float): the quantity of co2 produced by the engine, in g/km.
        fuel_type (string): the name of the fuel liquid.

    Returns:
        float: the estimated fuel consumption, in l/100km.
    """
    if fuel_type == 'diesel':
    	co2_mass_produced_by_fuel_combustion = 2640.0
    elif fuel_type == 'lpg':
    	co2_mass_produced_by_fuel_combustion = 1665.0
    else:
		co2_mass_produced_by_fuel_combustion = 2392.0
	return 100.0 * co2_emission / co2_mass_produced_by_fuel_combustion