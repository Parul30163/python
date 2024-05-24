import pandas as pd


it=pd.read_csv("is2.csv")

it

it.dtypes

it.head(10)

it.tail(10)

# what is descriptive statics
##count of value
##mean 
##sd
#min
#max
#3 %-1st,2nd ,3rd

it.describe()

it.describe(include='all')

it.info()

it['Sale Price'].mean()

it['Sale Price'].min()

it['Sale Price'].max()

it['Sale Price'].std()

it['Sale Price'].quantile(.25) #for percentile

it['Condition of the House'].unique()

import numpy as np

np.std(it['Sale Price'])

it['Sale Price'].std()-np.std(it['Sale Price'])

np.std(it['Sale Price'],ddof=1)

it['Sale Price'].std()

dir(np)

import matplotlib.pyplot as plt

plt.plot(it['Sale Price'])

plt.plot(it['Sale Price'], color ='green')
plt.xlabel("Record Numberrr")
plt.ylabel("Sale Pricree")
plt.title("my first graph")
plt.show()

plt.plot(it['Sale Price'],marker='o',markerfacecolor='Blue',markersize=5,color ='green',linewidth=5,linestyle='dashed')

it.groupby('Condition of the House')['ID'].count()

values=(500,1701,14031,5679,1172)

labels=('Bad','Excellent','Fair','Good','Okay')

plt.pie(values,labels=labels)

plt.bar(labels,values,color='green')

plt.bar(labels,values,color='green',linewidth=5,linestyle='dashed')
plt.xlabel("Record Numberrr")
plt.ylabel("Sale Pricree")
plt.title("my first graph")
plt.show()

it['Condition of the House'].value_counts().plot(kind='bar')# regex

