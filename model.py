# import tools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Models from sklearn
from flask import request
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Model Evaluation
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import plot_roc_curve

# Save the Random Forest Classification model for use in the front end
import pickle

# count of each target variable
from collections import Counter

# import data
wine = pd.read_csv('winequality-red.csv')

Counter(wine['quality'])

# add a rating of 1-3
# VGW wants to classify the wine into three categories for pricing...poor, average, and excellent. These next few cells
# will add a Ratings column to our data set.
# 1 - Poor
# 2 - Average
# 3 - Excellent
# Based on what the data says in the counter the wine will be classified in the following ways:
# 1,2,3 --> Poor
# 4,5,6,7 --> Average
# 8,9,10 --> Excellent

# Create an empty list called Rating to hold
ratings = []

for i in wine['quality']:
    if 1 <= i <= 3:
        ratings.append('1')
    elif 4 <= i <= 7:
        ratings.append('2')
    elif 8 <= i <= 10:
        ratings.append('3')
wine['rating'] = ratings

# MODELING
# Split the x and y variables
X = wine.iloc[:, :11]
y = wine['rating']

# What makes a wine poor, average, or excellent?
# split data into train and test sets
np.random.seed(42)

# Split the data into train and test groups
X_train, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.25)

# train and test with Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_predict = rf.predict(X_test)

# get importance
importance = rf.feature_importances_
# summarize feature importance
for i, v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i, v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(rf, open(filename, 'wb'))


# load the model from disk and return a prediction '1' || '2' || '3'
def get_prediction(user_input):
    if user_input.length == 11:
        loaded_model = pickle.load(open(filename, 'rb'))
        return loaded_model.predict([user_input])
    else:
        return "Something went wrong"
