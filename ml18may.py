import numpy as np
import pandas as pd 
df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\placement - placement.csv")
df

df.head()

df.tail()

df.describe()

df.info()

top_left_corner_df=df.iloc[:5,:3]
top_left_corner_df

s=df.axes 
s #no of rows

p= df.dtypes
p

b=df.empty # return true if data has missing value otherwise false
b

i=df.ndim#no of  axes D. (it is 2)
i

t=df.shape
t#shape= n(row , n(coulmn)) 

d=df.size#row count*column count
d

a=df.values #get numpy array of df
a 

df.copy()

p=df.sort_values(by='resume_score')
p

r=df.sort_index()
r

x=df.astype(int) #type conversion
x

x=df.astype(int) #type conversion
#x=df['cgpa'].astype(int) ### for single value change
x

x=df['cgpa'].astype(int) ### for single value change
x

t=df.add(4) #work on same datatype
t

a=df.abs()#abstract
a

df['cgpa']=df['cgpa'].add(4)
df

s=df.count()#count the total value
s

v=df.max()
v

p=df.min()
p

df.mean()

df.median() # no mode okk

df.sum()

a=df.filter(items=['cgpa','placed'])
a

df[['cgpa','placed']] #same as filter

a=df.filter(items=[5,6],axis=0)# row wise ..1 is column
a


a=df.filter(like='5',axis=0)# 5 in indexing
a

df.to_dict()#save in dict

df.to_string() #save in str

idx=df.columns
idx

df.columns[0]#first column name

df.columns.tolist() #list of column lble

df.columns.values#array of column name

df.rename(columns={'cgpa':'halfyearly'}) #rename column

df.rename(columns={'halfyearly':'cgpa'}) #rename column

df['half']=df['cgpa'].where(df['cgpa']>15,other=0)
df

# EDA ==> EXxploratory Data Analysis

# PArts of EDA
#1.Univariente Analysis > analysis on single independent column
 #2.bivariente a. >> on 2 columns
 #3.Multivarient a. >>on more then 2 column

#data type
#1. numerical data >> continous data 



import numpy as np
import pandas as pd

import matplotlib.pyplot as plt #visualization lib
import seaborn as sns #matplot's update version is seaborn


df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\titanic - titanic.csv")

df.head()

df.isnull().sum()

# 1.Univariante analysis

df.columns

df['Survived'].value_counts()

sns.countplot(x=df['Survived'])

df['Survived'].value_counts().plot(kind='bar') #bar type graph

df['Pclass'].value_counts()

sns.countplot(x=df['Pclass'])

df['Survived'].value_counts().plot(kind='pie',autopct='%.2f') #pie type graph

#.........catarogical column......... kthm

#if we have numerical data item  then we use histrogram
#coz it finds the distribution

plt.hist(df['Age'])


#2.displot
#curve is called>> KDE (kernal Desity Extraction)..>> denotes>> use to find problity

sns.distplot(df['Age'])

sns.distplot(df['Age'],hist=False)

#Boxplot
#for  find  our outliner
##..
#1 lower fence
#2 25% data
#3.IQR(inter quartile range )(75%-25%)
#4.75% data
#5. Upper fence

sns.boxplot(x=df['Age'])# jo do pt dekh re hai vo outliners hai

tips=pd.read_csv("C:\\Users\\PARUL\\Downloads\\tips - tips.csv")
tips

tips=sns.load_dataset('tips')
tips

# Bivariate Analysis

#1. scatterplot (Numerical column -Numerical column)

sns.scatterplot(x=tips['total_bill'],#df[total_bill]
               y=tips['tip'])

sns.scatterplot(x='total_bill',y='tip',data=tips,hue =tips['sex']) #hue ..on the bases of

sns.scatterplot(x='total_bill',y='tip',data=tips,hue =tips['sex'],style=tips['smoker'])

#HeatMap (catorigal-catrogical)
p=pd.crosstab(df['Pclass'],df['Survived'])
p

sns.heatmap(p)

((df.groupby('Pclass').mean()['Survived'])*100).plot(kind='bar')
#df.groupby('Pclass').mean().........groupby>>aggrate fun pr lag ta hai

#market fluction and pracdibity
#prblm... real state are highly volatile and influnced by a myriad of factors such as ecnomics condition ,interst rate, gov policies
#data analysis approch>>analysis histroical markect data , economic indicater and trend ti pridict future market  moments
###
#coustmor preference and behaviour...
#understing and predicting coustomer preferences for property features,location and price range is essintals for effective marketings and sales strages
###
#data analysis approch
#analysis customer data ,including search patterns,inquries ,past pucheses 
#u have to identify distint customer profile and preferences


