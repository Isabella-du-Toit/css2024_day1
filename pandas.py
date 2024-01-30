# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:55 2024

@author: Isabella
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes
"""

print(file.describe())

iris = pandas.read_csv("iris.csv")

print(iris)

print(iris.info())

print(iris.describe())

diab_data = pandas.read_csv("diab_data.csv")

print(diab_data)

print(diab_data.info())

print(diab_data.describe())

file_housing = pandas.read_csv("housing_data.csv")

print(file_housing)

print(file_housing.info())

print(iris.info())

print(iris.describe())

file2 = pandas.read_csv("insurance_data.csv", skiprows=5)
#data frame has text in first couple rows

print(file2)

print(file_housing.info())

print(file_housing.describe())

#file3 = pandas.read_csv("housing_data.csv", names = column_names)
#add column names

print(file_housing)

print(file_housing.info())



