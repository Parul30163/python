# encoding>> method to  converting caterogical  data to numeric
#1. Labelencodding >> using this method , we can covert our tagetor 1D data 

import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df.head(2)

df=df.dropna()

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df['gender']=lb.fit_transform(df['gender'])
df['cough']=lb.fit_transform(df['cough'])
df['city']=lb.fit_transform(df['city'])
df['has_covid']=lb.fit_transform(df['has_covid'])

df.sample(5)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

df_sc=sc.fit_transform(df)

#df_sc

df_new =pd.DataFrame(df_sc,columns=df.columns)

np.round(df.describe(),1)

import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\insurance - insurance.csv")

df.sample(5)

df=df.dropna()

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df['sex']=lb.fit_transform(df['sex'])
df['smoker']=lb.fit_transform(df['smoker'])
df['region']=lb.fit_transform(df['region'])


df.sample(5)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

df_sc=sc.fit_transform(df)

df_new=pd.DataFrame(df_sc,columns=df.columns)

np.round(df.describe())


x=df.drop(columns =['age'],axis=1)  ### independent columns
y=df['age'] ###Target column

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print(df.shape)
print(x.shape)
print(y.shape)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.preprocessing import MinMaxScaler

mn = MinMaxScaler() 

x_train_mn = mn.fit_transform(x_train) 

x_test_mn = mn.fit_transform(x_test) 

x_train_new=pd.DataFrame(x_train_mn,columns=x_train.columns)

np.round(x_train.describe(),1)







# 2.OrdinalEncoder



df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df.head()

df=df.drop(columns=['age','fever'])

df.head()

df['city'].value_counts()

from sklearn.preprocessing import OrdinalEncoder

oe= OrdinalEncoder(categories=[['Male','Female'],['Mild','Strong'],['Kolkata','Bangalore','Delhi','Mumbai'],['Yes','No']])

oe

oe.fit(df)

df_new=oe.transform(df)

oe.categories_

df_new

df=pd.DataFrame(df_new,columns=df.columns)

df.sample(7)

