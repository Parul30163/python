# Intro to ml

#process >> data preparation >> ml model>> performance evaulation

# 1. Data preparation

#data>> independent data(x)= dependent data(y)

#x=> x_train,x_test
       
#y=> y_train,y_test
         
#data prepare ==>ml model==> preformance evualation

import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\placement - placement.csv")

df.head()

df.shape

x= df.drop(columns=['placed'],axis=1)#independent
y=df['placed']#target

print(x.shape)
print(y.shape)

from sklearn. model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# standardization >> data mean =0,,standard devation=1

np.round(x_train.describe(),2)

from sklearn.preprocessing import StandardScaler



sc=StandardScaler()

x_train_sc=sc.fit_transform(x_train)#fit means learn the parameter and transform means apply changes on datas 

x_train_new=pd.DataFrame(x_train_sc,columns=x_train.columns)

x_train_new.head(3)

np.round(x_train_new.describe(),3)

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\insurance - insurance.csv")

df.head()

x=df.drop(columns=['charges'],axis=1)
y=df['charges']

from sklearn.model_selection import train_test_split

xx_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print(df.shape)
print(x.shape)
print(x_train.shape)
print(x_test.shape)
print(y.shape)
print(y_train.shape)
print(y_test.shape)

np.round(x_train.describe(),1)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()


x_train_sc=sc.fit_transform(x_train)

x_train_sc

x_train_new=pd.DataFrame(x_train_sc,columns=x_train.columns)

np.round(x_train_new.describe(),1)

# Normalization min=0, max=1

from sklearn.preprocessing import MinMaxScaler

mn=MinMaxScaler()

x_train_mn=mn.fit_transform(x_train)

x_train_new=pd.DataFrame(x_train_mn,columns=x_train.columns)

np.round(x_train.describe(),1)

np.round(x_train_new.describe(),1)

