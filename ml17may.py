# Pandas==> it is an open source lib. that is used for handle data manipulation

#data structure== 1. Series 2. Data Frames

import pandas as pd
a= pd.Series([10,3,85,66])
a

type(a)

# data frames

a={
    "emp":[1,2,3,4,5,6,7,8],# more then 5
    "name":['parul','manan','chinku','yash','kunal','purva','priyani','yashi'],
    "dep":['CEO','FOUNDER','it','it','it','it','it','hr'],
    "working":[8,9,5,6,7,9,9,9]
}

type(a)

df=pd.DataFrame(a)
df

df.columns

df.head() #it return first 5 rows

df.head(2)

df.tail() #it return bottom 5 rows


df.tail(2)

df.sample(4) #it returen random-indexed row

df.describe() #it descreibe statically view of data

df.info()#complet overview of data

#if you want to export your data in csv format

df.to_csv("D:\\regex2024\\ml exp\\emp_info.csv")

df.to_csv("D:\\regex2024\\ml exp\\new_emp_info.csv", index = False)

df.to_excel("D:\\regex2024\\ml exp\\old_emp_info.xlsx")

df=pd.read_csv("D:\\regex2024\\ml exp\\new_emp_info.csv")

df.head()

df['dep']

df['dep'].value_counts()

a={
    "emp":[1,2,3,4,5,6,7,8],# more then 5
    "name":['parul','manan','chinku','yash','kunal','purva','priyani','yashi'],
    "dep":['CEO','FOUNDER','it','it','it','it','it','hr'],
    "working":[8,9,5,6,7,9,9,9]
}

df=pd.DataFrame(a)
df

df['working'][3]=9

df.head()

# loc and iloc

#df.loc["row_range","column_range"]
#df.iloc["row_range,column_range"]

df.loc[2]

df.loc[2,"name"]

df.loc[2:5,["name","dep"]] #starting and end valu include

df.iloc[2]

df.iloc[2:5,1:3]

df.iloc[2,1]

df['name'][3]=None

df['dep'][6]=None

df['dep'][7]=None

df

df.isnull #it will return true if you have missing value  othewise false

df.isnull().sum() #we can check  total missing value using this command

df=df.dropna() # remove all the row of none value
df

