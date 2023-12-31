# -*- coding: utf-8 -*-
"""Breast cancer prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14gelO7a9Xf8tispXq9eAaOpANqxpJUor

## LIBRARIES
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from IPython.core.error import IPythonCoreError

import warnings
warnings.filterwarnings("ignore")

"""# DATASETS LOADING


"""

data = pd.read_csv('/content/drive/MyDrive/Breast cancer.csv')
data.head()

data.describe()

data.info()

data.shape,data.size

sns.pairplot(data=data, corner=True)
plt.show()

"""# TRAINING & TESTING"""

train= pd.read_csv('/content/drive/MyDrive/Breast cancer.csv')
test= pd.read_csv('/content/drive/MyDrive/Breast cancer.csv')

train.head()

test.head()

"""#Changing Axis values"""

data.set_axis(['Id','Diagnosis','Radius','Texture','Perimeter','Area','Smootheness','Compactness','Concavity','Concave_points','Symmetry','Fractal_dimension','Radius_se','Texture_se','Perimetr_se','Area_se','Smoothness_se','Compactness_se','Concavity_se','Concave_points_se','Symmetry_se','Fractal_dimension_se','Radius_worst','Texture_worst','Perimeter_worst','Area_worst','Smootheness_worst','Compactness_worst','Concavity_worst','Concave_points_worst','Symmetry_worst','Breast_cancer'], axis='columns',inplace=True)

data.head()

"""#DATA CLEANING & PROCESSING"""

data.isnull().sum()

train.isnull().sum()
print("Train Shape:",train.shape)
test.isnull().sum()
print("Test Shape:",test.shape)

test.info()

train.info()

plt.figure(figsize=(24,12))
sns.heatmap(data.corr(),annot=True,cmap='Blues')
plt.plot()

"""#EDA TESTING"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import plotly.express as px

fig=px.bar(data.head(10), x="Breast_cancer",y="Area",color="Concavity",template="ggplot2")
fig.show()

fig = px.pie(data, values='Radius', names='Diagnosis')
fig.show()

fig=px.bar(data.head(100),x='Area',y='Diagnosis',template='ggplot2')
fig.show()

fig = px.line(data, x="Radius", y="Id", color='Breast_cancer',markers=True,color_discrete_sequence=['White','orange'],template='plotly_dark')
fig.show()

df= data.copy()
df.head()

"""#LABEL ENCODING




"""

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Diagnosis']=le.fit_transform(df['Diagnosis'])
df['Breast_cancer']=le.fit_transform(df['Breast_cancer'])
df

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in df.columns:
    if df[i].dtype == 'object':
        df[i]=l.fit_transform(df[i])

X = df.drop('Diagnosis',axis=1)
y = df['Breast_cancer']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=2)

"""#LINEAR REGRESSION"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

"""# Evalulating training prediction"""

lr = LinearRegression()
lr.fit(xtrain, ytrain)

ytrain_pred = lr.predict(xtrain)

# evaluating the testing data

mse = mean_squared_error(ytrain, ytrain_pred)
rmse = (np.sqrt(mse))
r2 = r2_score(ytrain, ytrain_pred)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

"""# Evaluating Testing prediction

"""

ytest_pred = lr.predict(xtest)

mse = mean_squared_error(ytest, ytest_pred)
rmse = (np.sqrt(mean_squared_error(ytest, ytest_pred)))
r2 = r2_score(ytest, ytest_pred)

print("the model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

"""# Final conclusion"""

mean = data.mean
mean()

mean=data.mean
mean