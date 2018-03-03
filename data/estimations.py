#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Estimate missing information about the vehicles."""

from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

TRAIN_RATIO = 0.9
TEST_RATIO = 1.0 - TRAIN_RATIO

#####################################################################
# DATASET
#####################################################################

df = pd.read_csv('./vehicles.csv')

#####################################################################
# REMOVE ERRORS
#####################################################################

df = df[df['fuel_consumption'] > 0.0]
df = df[df['gross_weight'] > 0.0]
df = df[df['model'] == 'Vito']

#####################################################################
# VEHICLE MODELS
#####################################################################

model_list = list(set(df['model'].values))

#####################################################################
# DIFF GROSS WEIGHT
#####################################################################

min_gross_weight = {
    m: df.loc[df['model'] == m, 'gross_weight'].min()
    for m in model_list}

df['min_gross_weight'] = df['model'].apply(lambda m: min_gross_weight[m])
df['ratio_gross_weight'] = df['gross_weight']
df['ratio_gross_weight'] = df['ratio_gross_weight'].sub(df['min_gross_weight'], axis=0)
df['ratio_gross_weight'] = df['ratio_gross_weight'].divide(df['min_gross_weight'], axis=0)

#####################################################################
# DIFF CONSUMPTION
#####################################################################

min_consumption = {
    m: df.loc[df['model'] == m, 'fuel_consumption'].min()
    for m in model_list}

df['min_consumption'] = df['model'].apply(lambda m: min_consumption[m])
df['ratio_fuel_consumption'] = df['fuel_consumption']
df['ratio_fuel_consumption'] = df['ratio_fuel_consumption'].sub(df['min_consumption'], axis=0)
df['ratio_fuel_consumption'] = df['ratio_fuel_consumption'].divide(df['min_consumption'], axis=0)

#####################################################################
# IGNORE NAN & INFINITE
#####################################################################

# df = df[df['ratio_fuel_consumption'].map(pd.notnull)]
# df = df[df['ratio_gross_weight'].map(pd.notnull)]

df.dropna()

#####################################################################
# SPLIT BETWEEN TRAIN & TEST
#####################################################################

permuted_index = np.random.permutation(df.index.tolist())
split_index = int(TRAIN_RATIO * df.index.size)
train_index = permuted_index[:split_index]
test_index = permuted_index[split_index:]

train_df = df.loc[train_index]
test_df = df.loc[test_index]

#####################################################################
# CONSUMPTION VS EMISSIONS, WEIGHT
#####################################################################

fuel_type_train_index = train_df['fuel_type'] == 'Diesel'
fuel_type_test_index = test_df['fuel_type'] == 'Diesel'

x_train = train_df.loc[
    fuel_type_train_index,
    ['ratio_gross_weight']].values.reshape(-1, 1)
y_train = train_df.loc[
    fuel_type_train_index,
    ['ratio_fuel_consumption']].values.reshape(-1, 1)

x_test = test_df.loc[
    fuel_type_test_index,
    ['ratio_gross_weight']].values.reshape(-1, 1)
y_test = test_df.loc[
    fuel_type_test_index,
    ['ratio_fuel_consumption']].values.reshape(-1, 1)

#####################################################################
# TRAIN
#####################################################################

model = linear_model.LinearRegression()
model.fit(X=x_train, y=y_train)

#####################################################################
# TEST
#####################################################################

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

#####################################################################
# VIZ
#####################################################################

plt.scatter(
    x_test,
    y_test,
    color='black')

plt.plot(
    x_test,
    y_pred,
    color='blue',
    linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

print(model.coef_)