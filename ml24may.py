import numpy as np
import pandas as pd


df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df.head()

df.dropna()

df.drop(columns=['age','fever'])

df.head()

from sklearn.preprocessing import OneHotEncoder

df.shape

# get_dummies method

p=pd.get_dummies(df,columns=['gender','cough','city','has_covid'])

p.shape

p

p=pd.get_dummies(df,columns=['gender','cough','city','has_covid'],drop_first=True)

p.shape

ohe=OneHotEncoder (drop='first',sparse=False,dtype=np.int32)

df_new=ohe.fit_transform(df[['gender','cough','city','has_covid']])

df_new.shape

# column transformer

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.preprocessing import OrdinalEncoder

df= pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df

df.isnull().sum()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(df.drop(columns=['has_covid']),df['has_covid'],test_size=0.2)

x_train

# Manually type output

#adding simple imputer to fever column
si=SimpleImputer()
x_train_fever=si.fit_transform(x_train[['fever']])

#also the test data
x_test_fever=si.fit_transform(x_test[['fever']])

x_train_fever.shape

# ordinal encoding > cough

oe =OrdinalEncoder(categories =[['Mild','Strong']])
x_train_cough=oe.fit_transform(x_train[['cough']])

#also the test data

x_test_cough=oe.fit_transform(x_test[['cough']])

x_train_cough.shape


#OneHotEncoding>> gender,city
ohe=OneHotEncoder(drop='first',sparse=False)
x_train_gender_city=ohe.fit_transform(x_train[['gender','city']])

#also the test data
x_test_gender_city=ohe.fit_transform(x_test[['gender','city']])
x_train_gender_city.shape

#Extracting age
x_train_age=x_train.drop(columns=['gender','fever','cough','city']).values

#also the test data

x_test_age=x_test.drop(columns=['gender','fever','cough','city']).values


x_train_age.shape

x_train_transformed =np.concatenate((x_train_age, x_train_fever ,x_train_gender_city  ,x_train_cough),axis=1)

x_train_transformed.shape

# by the help of column transformer

from sklearn.compose import ColumnTransformer #this is how to import

transformer= ColumnTransformer(transformers=[
    ('tnf1',SimpleImputer(),['fever']),  
    ('tnf2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),
    ('tnf3',OneHotEncoder(sparse=False,drop='first'),['gender','city'])
],remainder='passthrough')#reminder= passthrough>> it means rest all the column remain same

transformer.fit_transform(x_train).shape


transformer.fit_transform(x_test).shape


# Function TRansformer

#we can pass our costom cond on an array

from sklearn.preprocessing import FunctionTransformer
import numpy as np

#create a datbase
X=np.array([[1,2],[3,4]])

#define the transformation fun
log_transform=FunctionTransformer(np.log1p)

#define the transformer to the dataset
X_transformed=log_transform.transform(X)

#view the transform data
print(X_transformed)


#eg 2
def my_feature_engineering(X):
    return np.hstack((X,X**2))

#create a FunctionTransformer to apply the current fun
custom_transformer= FunctionTransformer(my_feature_engineering)

#apply the transformer to the input data
X_transformed =custom_transformer.transform(X)

#view
print(X_transformed)

#eg 3
def my_scaling(X):
    return X/np.max(X)

#create a FunctionTransformer to apply the current fun
custom_transformer= FunctionTransformer(my_scaling)

#apply the transformer to the input data
X_transformed =custom_transformer.transform(X)

#view
print(X_transformed)

#eg4
X=np.array ([[1,2],[3,np.nan]])
def my_cleaning(X):
    X[np.isnan(X)]=0
    return X

#create a FunctionTransformer to apply the current fun
custom_transformer= FunctionTransformer(my_cleaning)

#apply the transformer to the input data
X_transformed =custom_transformer.transform(X)

#view
print(X_transformed)


