# Decision tree alogrithm
#supervised ml algo..

#target data ==

#categorical== decision treeclassifier()

#numerical == decisiontreeregressor

import numpy as np 
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df=df.dropna()

from sklearn.preprocessing import  LabelEncoder

lb= LabelEncoder()

df['gender']=lb.fit_transform(df['gender'])
df['cough']=lb.fit_transform(df['cough'])
df['city']=lb.fit_transform(df['city'])
df['has_covid']=lb.fit_transform(df['has_covid'])

df.head()

x=df.drop(columns=['has_covid'])
y=df['has_covid']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier()

dt.fit(x_train,y_train)

y_pred=dt.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\tips - tips.csv")

df.head()

from sklearn.preprocessing import LabelEncoder

df['sex']=lb.fit_transform(df['sex'])
df['smoker']=lb.fit_transform(df['smoker'])
df['day']=lb.fit_transform(df['day'])
df['time']=lb.fit_transform(df['time'])

df.head()

x=df.drop(columns=['total_bill'],axis=1)
y=df['total_bill']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeRegressor

dt=DecisionTreeRegressor()

dt.fit(x_train,y_train)

y_pred=dt.predict(x_test)

from sklearn.metrics import r2_score

r2_score(y_test, y_pred)

import numpy as np 
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\insurance - insurance.csv")

df.head()

