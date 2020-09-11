#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the fuel consumption tools."""

from __future__ import absolute_import, division, print_function

from numpy import isclose

from homespace.references import vehicules

def test_conversions_mpg_to_lpkm():
    assert vehicules.us_mpg_to_lpkm(0.0) == 0.0
    assert vehicules.imp_mpg_to_lpkm(0.0) == 0.0

    assert isclose(vehicules.us_mpg_to_lpkm(1.0), 235.215, rtol=1e-3)
    assert isclose(vehicules.imp_mpg_to_lpkm(1.0), 282.481, rtol=1e-3)

def test_conversions_lpkm_to_mpg():
    assert vehicules.lpkm_to_us_mpg(1.0) == 0.0
    assert vehicules.lpkm_to_imp_mpg(1.0) == 0.0

    assert isclose(vehicules.lpkm_to_us_mpg(1.0), 235.215, rtol=1e-3)
    assert isclose(vehicules.lpkm_to_imp_mpg(1.0), 282.481, rtol=1e-3)
