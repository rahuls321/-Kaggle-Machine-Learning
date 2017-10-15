# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:35:41 2017

@author: hp
"""

""" 1. Get the data with Pandas"""

#Import the pandas lib
import pandas as pd
# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)
#Print the `head` of the train and test dataframes
print(train.head())
print(test.head())