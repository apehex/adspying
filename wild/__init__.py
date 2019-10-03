# -*- coding: utf-8 -*-

"""
========
Wild Ads
========

Find the most relevant ads from heterogeneous sources.
"""

from __future__ import absolute_import, division, print_function

import os

import numpy as np
import pandas as pd

#####################################################################
# CONTENT
#####################################################################

__author__ = """apehex"""
__email__ = 'apehex@protonmail.com'
__version__ = '0.1.0'

__all__ = []

#####################################################################
# SCRIPT PATH
#####################################################################

_INIT_SCRIPT_PATH = os.path.realpath(__file__)
_INIT_DIR_PATH = os.path.dirname(_INIT_SCRIPT_PATH)
_MAKE_DATA_PATH = os.path.join(
    _INIT_DIR_PATH,
    './data/make.csv')
_MODEL_DATA_PATH = os.path.join(
    _INIT_DIR_PATH,
    './data/model.csv')
_VEHICLE_DATA_PATH = os.path.join(
    _INIT_DIR_PATH,
    './data/vehicle.csv')

#####################################################################
# REFERENTIALS
#####################################################################

MAKE_REFERENTIAL = pd.read_csv(
    _MAKE_DATA_PATH,
    encoding='utf-8',
    dtype={'make': str},
    header=0)

MODEL_REFERENTIAL = pd.read_csv(
    _MODEL_DATA_PATH,
    encoding='utf-8',
    dtype={'make': str, 'model': str},
    header=0)

VEHICLE_REFERENTIAL = pd.read_csv(
    _VEHICLE_DATA_PATH,
    encoding='utf-8',
    dtype={
        'make': str,
        'model': str,
        'category': str,
        'gross_weight': np.float64,
        'wheel_base': np.float64,
        'track_width': np.float64,
        'fuel_type': str,
        'engine_power': np.float64,
        'co2_emission': np.float64,
        'electric_consumption': np.float64,
        'fuel_consumption': np.float64},
    header=0)
