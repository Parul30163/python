# k-means clusturing

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#generate synthetic data
np.random.seed(0)
n_samples=200
n_clusters=4
X=np.random.rand(n_samples,2)*10

#create k-mean clustering model
kmeans=KMeans(n_clusters=n_clusters)
kmeans.fit(X)

#get cluster labels and centers
labels=kmeans.labels_
centers= kmeans.cluster_centers_

#visualize the clusters
plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1],c=labels,
           cmap='viridis',edgecolor='k')
plt.scatter(centers[:,0],centers[:,1],
           c='red',marker='x',s=200)
plt.title('K-means clustring')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()

import numpy as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\mall.csv")

df.head()

df = df.drop(columns = ['CustomerID' , 'Genre' ])

df.head() 

x = df.iloc[: , [0,1]].values

from sklearn.cluster import KMeans 

import matplotlib.pyplot as plt 

a = [] 

for i in range(1,11):
    b = KMeans(n_clusters = i , init = 'k-means++' , random_state = 42) 
    b.fit(x) 
    a.append(b.inertia_)
    
plt.plot(range(1,11) , a) 

plt.title('The Elobw Method Graph')  
plt.xlabel('Number of clusters(k)')  
plt.ylabel('wcss_list')  
plt.show()  

# From the above plot, we can see the elbow point is at 4. So the number of clusters here will be 4.

b = KMeans(n_clusters=4, init='k-means++', random_state= 42)  
y_predict= b.fit_predict(x) 

#visulaizing the clusters  
plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1') #for first cluster  
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2') #for second cluster  
plt.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3') #for third cluster  
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4') #for fourth cluster  
 
plt.scatter(b.cluster_centers_[:, 0], b.cluster_centers_[:, 1], s = 300, c = 'yellow', 
            label = 'Centroid')   
plt.title('Clusters of customers')  
plt.xlabel('Annual Income (k$)')  
plt.ylabel('Spending Score (1-100)')  
plt.legend()  
plt.show()  

