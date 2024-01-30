# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:26:52 2024

@author: Isabella
"""

import pandas

file = pandas.read_csv("grade_analysis.csv")

print(file)
print(file.info())
print(file.describe())
print(file["grade"]>75)
print(file["grade"].max())


