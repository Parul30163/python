import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\market_basket.csv",header=None)

df.head()

df.shape

#
# pip install apyori

#data processing
transactions=[]
for i in range (0,7501):
    transactions.append([str(df.values[i,j])for j in range(0,20)])
    
#training the dataset
from apyori import apriori
rules = apriori (transactions,
                min_support =0.003,     #(3items*7 days in week )/(total rows in dataset 7501)
                min_confidence=0.2,
                min_left=3,
                min_length=2)
#visualizing the results
a=list(rules)
result= [list(a[i][0])for i in range(0,len(a))]

a

result


