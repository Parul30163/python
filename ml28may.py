#RandomForest MOdel ==> Supervised ml model
# 1 R.F.  ===> `100 DECISIO TREE MODEL 
# Target data Categorical ===> R.F.Classifier() ====> 100 dt ===> 70 yes , 30 no ===>
# majority ==> final prediction (yes)

# Target data Numerical ====>  R.F.Regressor() ====> mean > value ===> final prediction


import numpy as np 
import pandas as pd 

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\Social_Network_Ads - Social_Network_Ads.csv")

df.head(2)

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder() 

df['Gender'] = lb.fit_transform(df['Gender'])

df.head()

x = df.drop(columns = ['Purchased'] , axis = 1)
y = df['Purchased']

from sklearn.model_selection import train_test_split 

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)

from sklearn.ensemble import RandomForestClassifier 

rf = RandomForestClassifier() 

rf.fit(x_train , y_train) 

y_pred = rf.predict(x_test)

from sklearn.metrics import accuracy_score 

accuracy_score(y_test , y_pred)

from sklearn.linear_model import LogisticRegression 

lr = LogisticRegression() 

lr.fit(x_train , y_train) 

y_pred = lr.predict(x_test)

accuracy_score(y_test , y_pred)

from sklearn.tree import DecisionTreeClassifier 

dt = DecisionTreeClassifier() 

dt.fit(x_train , y_train)

y_pred = dt.predict(x_test)

accuracy_score(y_test , y_pred)

# RandomForestRegressor

df = pd.read_csv("C:\\Users\\PARUL\\Downloads\\tips - tips.csv")

df.head(2)

from sklearn.preprocessing import LabelEncoder 

lb = LabelEncoder() 

df['sex'] = lb.fit_transform(df['sex'])
df['smoker'] = lb.fit_transform(df['smoker'])
df['day'] = lb.fit_transform(df['day'])
df['time'] = lb.fit_transform(df['time'])

df.head(2) 

x = df.drop(columns = ['total_bill'] , axis = 1)
y = df['total_bill']

from sklearn.model_selection import train_test_split 

from sklearn.linear_model import LinearRegression 

lr= LinearRegression()

lr.fit(x_train , y_train) 

y_pred = lr.predict(x_test)

from sklearn.metrics import r2_score 

r2_score(y_test , y_pred)

from sklearn.tree import DecisionTreeRegressor 

dt = DecisionTreeRegressor() 

dt.fit(x_train , y_train) 

y_pred= dt.predict(x_test)

r2_score(y_test , y_pred)

from sklearn.ensemble import RandomForestClassifier 

rf = RandomForestClassifier() 

rf.fit(x_train , y_train) 

y_pred = rf.predict(x_test)

r2_score(y_test , y_pred)

# TASK ON COVID

