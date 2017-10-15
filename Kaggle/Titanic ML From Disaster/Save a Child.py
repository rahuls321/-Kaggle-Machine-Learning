# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:38:53 2017

@author: hp
"""

"""4. Does Age Play A Role"""

import pandas as pd

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

#No. of child survived under 18 or over 18

# Create the column Child and assign to 'NaN'
train["Child"] = float('NaN')

# Assign 1 to passengers under 18, 0 to those 18 or older. Print the new column.
train["Child"][train["Age"] >= 18] = 0
train["Child"][train["Age"] < 18] = 1

# Print the Survival Proportion over age 18
print(train["Survived"][train["Child"] == 1].value_counts())
# Print normalized Survival Rates for passengers under 18
print(train["Survived"][train["Child"] == 1].value_counts(normalize = True))

# Print normalized Survival Rates for passengers 18 or older
print(train["Survived"][train["Child"] == 0].value_counts(normalize = True))

