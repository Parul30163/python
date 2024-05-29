import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\newplacementdata - newplacementdata.csv")

df.head()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15,5))
plt.subplot(121)
sns.distplot(df['cgpa'])
plt.subplot(122)
sns.distplot(df['placement_exam_marks'])
plt.show()

sns.boxplot(df['placement_exam_marks'])

#finding IRQ
percentile25=df['placement_exam_marks'].quantile(0.25)

percentile75=df['placement_exam_marks'].quantile(0.75)

percentile25

percentile75

IQR=percentile75-percentile25
IQR

upper_limit=percentile75+1.5*IQR
upper_limit

lower_limit=percentile25-1.5*IQR
lower_limit

# Finding our outliners

df[df['placement_exam_marks']>upper_limit]

df[df['placement_exam_marks']<lower_limit]

#trimming (removeing outliner technique1)

newdf=df[df['placement_exam_marks']<upper_limit]


newdf

#comparision

plt.figure(figsize=(15,5))
plt.subplot(221)
sns.distplot(df['placement_exam_marks'])

plt.subplot(222)
sns.boxplot(df['placement_exam_marks'])

plt.subplot(223)
sns.distplot(newdf['placement_exam_marks'])

plt.subplot(224)
sns.boxplot(newdf['placement_exam_marks'])

plt.show()



#capping( tech2)

new_df_cap=df.copy()


#min=5  max=15
#min=4,3,1
#max=20,30,50
# new min=1
#new max=50


new_df_cap['placement_exam_marks']=np.where(
    new_df_cap['placement_exam_marks']>upper_limit,
    upper_limit,
  np.where(
  new_df_cap['placement_exam_marks']< lower_limit,
  lower_limit,
  new_df_cap['placement_exam_marks']))

new_df_cap

plt.figure(figsize=(15,8))
plt.subplot(221)
sns.distplot(df['placement_exam_marks'])

plt.subplot(222)
sns.boxplot(df['placement_exam_marks'])

plt.subplot(223)
sns.distplot(new_df_cap['placement_exam_marks'])

plt.subplot(224)
sns.boxplot(new_df_cap['placement_exam_marks'])

plt.show()

