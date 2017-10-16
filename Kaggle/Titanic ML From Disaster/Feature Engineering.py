# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:02:01 2017

@author: hp
"""
"""10. Feature-engineering for our Titanic data set"""
# Create train_two with the newly defined feature
train_two = train.copy()
train_two["family_size"] = 1 +train_two["SibSp"] + train_two["Parch"]

# Create a new feature set and add the new feature
features_three = train_two[["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch", "family_size"]].values

# Define the tree classifier, then fit the model
my_tree_three = tree.DecisionTreeClassifier()
my_tree_three = my_tree_three.fit(features_three, target)

# Print the score of this decision tree
print(my_tree_three.score(features_three, target))
