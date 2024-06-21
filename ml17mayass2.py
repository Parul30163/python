import pandas as pd
df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\covid_toy - covid_toy.csv")

df.head()

df['city']

df['city'].value_counts()

df['has_covid'][3]='yes'

df

df.loc[2]

df.loc[2:5,["gender","city"]]

df.iloc[2:5,1:3]

df['gender'][3]=None

df['city'][6]=None

df.head(10)

df.isnull

df.isnull().sum()


df=df.dropna()
df

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\insurance - insurance.csv")

df.head()

df['smoker']

df['smoker'].value_counts()

df['sex'][3]='female'

df['children'][3]=4

df.loc[2:5,["age","children"]]

df.iloc[2:5,1:3]

df['sex'][6]=None

df['age'][3]=None

df.head(10)

df.isnull

df.isnull().sum() 

df=df.dropna() 
df

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\placement - placement.csv")

df.head()

df['cgpa']

df['cgpa'].value_counts

df['placed'][3]=2

df

df.loc[1:10,["placed"]] 

df.iloc[2:5,1:3]

df['cgpa'][3]=None

df.isnull().sum()

df=df.dropna() 
df

