# naive bias

import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\Social_Network_Ads - Social_Network_Ads.csv",usecols=['Age','EstimatedSalary','Purchased'])

df.head()

x=df.drop(columns=['Purchased'])#independent column
y=df['Purchased']#dependent

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=23)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

x_train_new=sc.fit_transform(x_train)

x_test_new=sc.fit_transform(x_test)

#from sklearn.naive_bayes import BurnolliNb
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB

classifier =GaussianNB()

classifier.fit(x_train_new,y_train)

y_pred=classifier.predict(x_test_new)

y_pred

from sklearn.metrics import confusion_matrix

cn=confusion_matrix(y_test,y_pred)

cn

#[[tp,fn]
 #[fp,tn]]

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

from sklearn.ensemble import RandomForestClassifier 

rf = RandomForestClassifier() 

rf.fit(x_train , y_train) 

y_pred = rf.predict(x_test)

