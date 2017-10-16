# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:50:42 2017

@author: hp
"""


""" 12. Interpreting and Compairing """

#Request and print the `.feature_importances_` attribute
print(my_tree_two.feature_importances_)
print(my_forest.feature_importances_)

#Compute and print the mean accuracy score for both models
print(my_tree_two.score(features_two, target))
print(my_forest.score(features_two, target))

