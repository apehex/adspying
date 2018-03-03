#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Clean the raw data on vehicles, insurance, etc."""

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

#####################################################################
# TOOLS
#####################################################################

def format_string(unicode_bytes):
    return unicode_bytes.encode('utf-8', 'ignore').lower()

#####################################################################
# MERGED DF HEADERS
#####################################################################

INPUT_TO_OUTPUT_HEADERS_MAPPING = {
    'mk': 'manufacturer',
    'manufacturer': 'manufacturer',
    'cn': 'model',
    'model': 'model',
    'ct': 'category',
    'm (kg)': 'gross_weight',
    'vehicle gross weight': 'gross_weight',
    'w (mm)': 'wheel_base',
    'at1 (mm)': 'track_width',
    'ft': 'fuel_type',
    'fuel type': 'fuel_type',
    'ep (kw)': 'engine_power',
    'power (kw)': 'engine_power',
    'e (g/km)': 'co2_emissions',
    'co2': 'co2_emissions',
    'combined litres': 'fuel_consumption',
    'z (wh/km)': 'electric_consumption'
}

COLUMN_CONVERTERS = {
    'mk': format_string,
    'manufacturer': format_string,
    'cn': format_string,
    'model': format_string,
    'ct': format_string,
    'm (kg)': np.float64,
    'vehicle gross weight': np.float64,
    'w (mm)': np.float64,
    'at1 (mm)': np.float64,
    'ft': format_string,
    'fuel type': format_string,
    'ep (kw)': np.float64,
    'power (kw)': np.float64,
    'e (g/km)': np.float64,
    'co2': np.float64,
    'combined litres': np.float64,
    'z (wh/km)': np.float64
}

RATING_HEADERS = [
'consumption_rating',
'emission_rating',
'price_rating',
'size_rating']

#####################################################################
# READING
#####################################################################

van_df = pd.read_csv('./van/van-data.csv', encoding='utf-8')
auto_df = pd.read_csv('./van/co2_passenger_cars_v14.csv', sep='\t', encoding='utf-16')

#####################################################################
# SELECT COLUMNS
#####################################################################

van_df.rename(columns=format_string, inplace=True)
van_df.rename(columns=INPUT_TO_OUTPUT_HEADERS_MAPPING, inplace=True)

auto_df.rename(columns=format_string, inplace=True)
auto_df.rename(columns=INPUT_TO_OUTPUT_HEADERS_MAPPING, inplace=True)

print(van_df.columns.values)
print(auto_df.columns.values)

#####################################################################
# SWAPING MPG & L/100km
#####################################################################

error_index = van_df['fuel_consumption'] > 30.0
lpkm_headers = ['urban litres', 'extra urban litres', 'fuel_consumption']
mpg_headers = ['urban mpg', 'extra urban mpg', 'combined mpg']

van_df.loc[error_index, lpkm_headers + mpg_headers] = van_df.loc[error_index, mpg_headers + lpkm_headers].values

#####################################################################
# REMOVING OUTLIERS
#####################################################################

#####################################################################
# DEDUPING
#####################################################################

#####################################################################
# NORMALISING
#####################################################################

# # Create a minimum and maximum processor object
# min_max_scaler = preprocessing.MinMaxScaler()

# # Create an object to transform the data to fit minmax processor
# x_scaled = min_max_scaler.fit_transform(x)

# # Run the normalizer on the dataframe
# van_df = pd.DataFrame(x_scaled)

#####################################################################
# WRITING TO HD
#####################################################################

output_column_headers = INPUT_TO_OUTPUT_HEADERS_MAPPING.values()
output_column_headers = list(set(output_column_headers))

van_df.to_csv('vehicles.csv', columns=output_column_headers, index=False)