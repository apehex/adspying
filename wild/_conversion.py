################################################################################
# CONSTANTS
################################################################################

US_GALLON = 3.785412	# l
IMP_GALLON = 4.54609	# l
MILE = 1.609344	# km

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