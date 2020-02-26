# -*- coding: utf-8 -*-

"""
===================
Vehicules reference
===================

Consolidate data on the most common vehicules.
"""

from __future__ import absolute_import, division, print_function

import pandas as pd

from homespace._wrangling import format_number, format_text

#####################################################################
# META DATA
#####################################################################

INPUT_TO_OUTPUT_HEADERS_MAPPING = {
    'van-data.csv': {
        'manufacturer': 'make',
        'model': 'model',
        'vehicle gross weight': 'gross_weight',
        'fuel type': 'fuel_type',
        'power (kw)': 'engine_power',
        'co2': 'co2_emission',
        'combined litres': 'fuel_consumption',},
    'co2_passenger_cars_v14.csv': {
        'mk': 'make',
        'cn': 'model',
        'ct': 'category',
        'm (kg)': 'gross_weight',
        'w (mm)': 'wheel_base',
        'at1 (mm)': 'track_width',
        'ft': 'fuel_type',
        'ep (kw)': 'engine_power',
        'e (g/km)': 'co2_emission',
        'z (wh/km)': 'electric_consumption',
        'ft + e': 'fuel_consumption'}}      # added to the df

COLUMN_CONVERTERS = {
    'van-data.csv': {
        'Manufacturer': format_text,
        'Model': format_text,
        'Vehicle Gross Weight': format_number,
        'Fuel Type': format_text,
        'Power (kw)': format_number,
        'CO2': format_number,
        'Combined Litres': format_number,},
    'co2_passenger_cars_v14.csv': {
        'Mk': format_text,
        'Cn': format_text,
        'Ct': format_text,
        'm (kg)': format_number,
        'w (mm)': format_number,
        'at1 (mm)': format_number,
        'Ft': format_text,
        'ep (KW)': format_number,
        'e (g/km)': format_number,
        'z (Wh/km)': format_number}}

#####################################################################
# READING
#####################################################################

van_df = pd.read_csv(
    './data/raw/van-data.csv',
    encoding='utf-8',
    # usecols=COLUMN_CONVERTERS['van-data.csv'].keys(),
    converters=COLUMN_CONVERTERS['van-data.csv'],
    error_bad_lines=False)

auto_df = pd.read_csv(
    './data/raw/co2_passenger_cars_v14.csv',
    sep='\t',
    encoding='utf-16',
    usecols=COLUMN_CONVERTERS['co2_passenger_cars_v14.csv'].keys(),
    converters=COLUMN_CONVERTERS['co2_passenger_cars_v14.csv'],
    error_bad_lines=False)

make_df = pd.read_csv(
    'references/data/make.csv',
    encoding='utf-8',
    converters={0: format_text},
    header=None)

#####################################################################
# SELECT COLUMNS
#####################################################################

van_df.rename(
    columns=format_text,
    inplace=True)
van_df.rename(
    columns=INPUT_TO_OUTPUT_HEADERS_MAPPING['van-data.csv'],
    inplace=True)

auto_df.rename(
    columns=format_text,
    inplace=True)
auto_df.rename(
    columns=INPUT_TO_OUTPUT_HEADERS_MAPPING['co2_passenger_cars_v14.csv'],
    inplace=True)

#####################################################################
# REPLACE NANs
#####################################################################

auto_df.electric_consumption.fillna(value=0.0, inplace=True)

#####################################################################
# CORRECT ERRORS
#####################################################################

#####################################################################
# SWAPING MPG & L/100km
#####################################################################

error_index = van_df['fuel_consumption'] > 30.0
lpkm_headers = ['urban litres', 'extra urban litres', 'fuel_consumption']
mpg_headers = ['urban mpg', 'extra urban mpg', 'combined mpg']

van_df.loc[error_index, lpkm_headers + mpg_headers] = van_df.loc[error_index, mpg_headers + lpkm_headers].values

#####################################################################
# SIMPLIFY NOMENCLATURE
#####################################################################

make_old = list(set(auto_df.make.values))
make_references = list(make_df[0].values)

replace_make_dict = {
    old: find_closest_reference(
        target=old,
        candidates=make_references)
    for old in make_old}

replace_make_dict = {
    old: new
    for old, new in replace_make_dict.items()
    if old != new}

auto_df.replace(
    to_replace={'make': replace_make_dict},
    inplace=True)

#####################################################################
# REMOVING NAN
#####################################################################

van_df.dropna(how='any', inplace=True)
auto_df.dropna(how='any', inplace=True)

#####################################################################
# DEDUPING
#####################################################################

van_df.drop_duplicates(inplace=True)
auto_df.drop_duplicates(inplace=True)

#####################################################################
# ADD FUEL CONSUMPTION
#####################################################################

auto_df['fuel_consumption'] = auto_df.apply(
    lambda df: estimate_consumption_from_emission(
        co2_emission=df['co2_emission'],
        fuel_type=df['fuel_type']),
    axis=1)

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

output_column_headers = {
    'van-data.csv': INPUT_TO_OUTPUT_HEADERS_MAPPING['van-data.csv'].values(),
    'co2_passenger_cars_v14.csv': INPUT_TO_OUTPUT_HEADERS_MAPPING['co2_passenger_cars_v14.csv'].values()}

van_df.to_csv(
    'references/data/van_emission-consumption.csv',
    columns=output_column_headers['van-data.csv'],
    index=False)

auto_df.to_csv(
    'references/data/vehicles.csv',
    columns=output_column_headers['co2_passenger_cars_v14.csv'],
    index=False)