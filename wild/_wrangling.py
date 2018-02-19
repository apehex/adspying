from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

###############################################################################
# MERGED DF HEADERS
###############################################################################

MODEL_HEADERS = [
'manufacturer',
'model',
'variant',
'type',
'year_min',
'year_max']

SIZE_HEADERS = [
'mass',
'track_width',
'wheel_base']

PRICE_HEADERS = [
'price_new']

ENGINE_HEADERS = [
'fuel_type',
'fuel_mode',
'engine_capacity']
        
CONSUMPTION_HEADERS = [
'fuel_consumption',
'electricity_consumption']

EMISSION_HEADERS = [
'co2_emissions',
'nox_emissions', 'mass']

RATING_HEADERS = [
'consumption_rating',
'emission_rating',
'price_rating',
'size_rating']


###############################################################################
# READING
###############################################################################

DF = pd.read_csv('../data/raw/van-data.csv')

###############################################################################
# SWAPING MPG / L/100km
###############################################################################

df = pd.read_csv('van-data.csv')
erroneous_lpkm = df[df['Combined Litres'] > 30.0][['Urban Litres', 'Extra Urban Litres', 'Combined Litres']]
erroneous_mpg = df[df['Combined Litres'] > 30.0][['Urban MPG', 'Extra Urban MPG', 'Combined MPG']]

df.loc[df['Combined Litres'] > 30.0][['Urban Litres', 'Extra Urban Litres', 'Combined Litres']] = erroneous_mpg
df.loc[df['Combined Litres'] > 30.0][['Urban MPG', 'Extra Urban MPG', 'Combined MPG']] = erroneous_lpkm

###############################################################################
# REMOVING OUTLIERS
###############################################################################

###############################################################################
# DEDUPING
###############################################################################

###############################################################################
# NORMALISING
###############################################################################

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
