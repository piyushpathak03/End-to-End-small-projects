import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
pd.pandas.set_option('display.max_columns',None)

#Importing Dataset
data = pd.read_csv("alcohol-quality-data.csv")
dataset = data.copy()

#Preparing Data
Y = pd.DataFrame(dataset['Quality_Category'].replace({"Low":0,"High":1}))
X = dataset.drop(columns=['Quality_Category','pH','density'])

# Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

# Applying KNN
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=125)
clf.fit(X_train,np.ravel(y_train))
prediction = clf.predict(X_test)

# Getting Accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(prediction,np.ravel(y_test))

# Model 
import pickle
pickle.dump(clf,open('model.pkl','wb'))
