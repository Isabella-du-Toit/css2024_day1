# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:43 2024

@author: Isabella
"""

"""
Storing data in python
1. lists
2. dictionaries
3. data frames - spesific to pandas
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

#make variables manually
age1 = 30
age2 = 25
age3 = 29

#list - make many variables in list as one using block brackets
age = [30, 25, 29, 46, 22]

print(age)

"""
[30, 25, 29, 46, 22]
"""

#first age position strats at 0 = 30
print(age[0])

print(age[1])

#minimum from list age = 22
print(min(age))

#getting average - must give formula
avg = sum(age)/len(age)
print(avg)

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M, F, M"]
print(gender)

#range from first (0) to n-1
print(age[0:2])
"""
[30, 25]
"""

print(age[0:3])

#add number to list - append
age.append(100)
print(age)

#last value in list
print(age[-1])


#column names
names = ["A, B, C"]

file = pandas.read_csv("housing_data.csv", names = ["A, B, C"])
print(file)

#insert
print(age)
age.insert(0,100)

"""
Dictionaries - key: value pairs
cat: "a cute animal"
curly brackets
"""

mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"} 

#search in dictionary
print(mammals["cat"])

"""
Data frames
curly and block brackets
"""

#df = data frame

"""
import pandas
import pandas as pd - allow to use pd instead of pandas everytime
"""

import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

print(df["gender"])
print(df["country"])

print(df["age"].min())
print(df["age"].max())

#filter larger/smaller than
print(df["age"]>25)
print(df["age"]<25)

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)