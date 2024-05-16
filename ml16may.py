

# diag>>this function create a 2D array with all the digonal elenmentas the given and rest are zero

import numpy as np
a=np.diag([1,4,3,9])#list or tuple
a

# randint>> this function is used to genrate a ranmdom no between a given range

# syntax>> randint(min_value,max_value,total_no)

import numpy as np
a=np.random.randint(1,10,3)
a

# rand>> this function is used to genrate a random no between 0 to 1

# syntax>> rand(number of value)

import numpy as np
a=np.random.rand(5)
a

# randn().. thi sfunction is used to genrate a eandom no from -3 to 3. this may return positive or neg. no as well

# syntax>> random.randn(no of value)

import numpy as np
a=np.random.randn(5)
a

# reshaping data

import numpy as np
a=np.random.randint(1,50,12)
a

#n(rows)*n(column)=n(total no)


a.shape

a=a.reshape(2,6)
a

a=a.reshape(6,2)
a

a=a.reshape(3,4)
a

a=a.reshape(4,3)
a

a=a.reshape(12,1)
a

import numpy as np
a=np.random.randint(1,100,64)
a

a.shape#1, 64), (2, 32), (4, 16), and (8, 8).

a=a.reshape(1,64)
a

a=a.reshape(2,32)
a

a=a.reshape(4,16)
a

a=a.reshape(8,8)
a

# principle of -1

a=a.reshape(-1,8)
a

a=a.reshape(-1,16)
a

a=a.reshape(4,-1)
a

# seed function>> we know that randint fun generate random no. everytime we run the program , new set of random no i s genrated .so ,solve this problem we will use seed fun

import numpy as np

np.random.seed(8)
a=np.random.randint(1,10,3)
a

# view vs copy>> when we sclice a sub array from an array ,if may be done by two ways

import numpy as np
a=np.array([10,20,30,40,50,60,70,80])
b=a[3:6]
b[:]=0
a

b

# copy

import numpy as np
a=np.array([10,20,30,40,50,60,70,80])
b=a[3:6].copy()
b[:]=0
a


b

# conditional statenment

import numpy as np
a=np.arange(1,16)
a

a>10

a<10

b=a<10
b

b=a>10
b

a[a%2==0]


# operations on array

import numpy as np
a=np.arange(1,5)
a*2

a+2

a**2

a=np.array([1,4,9,16]).reshape(2,2)
a

b=np.array([5,6,7,8]).reshape(2,2)
b

a+b

b-a

b/a

a*b#simple multi jo kam k nhi hai

a.dot(b)#matrix multiplaction

# some other function

import numpy as np
a=np.array([10,20,30,40,50])
np.min(a)# min  value in array

np.max(a)

np.argmin(a)# min value in index

np.argmax(a)

np.sqrt(a)

np.sin(a)

# linspace>> this function return value between a given range and with a same gap between consicutive 

import numpy as np

a=np.linspace(1,2,5)# gap will be equal
a

# np.unique(arr,return_index=true, return_count=True)
return 3 array  1 the array with unique value 2.  array with respective index 3. aray with count of freq

a=np.array([10,20,30,40,10,20,50])
np.unique (a,True,True)

# horizontal and vertical atacking

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
a

b

np.hstack((a,b))

np.vstack((a,b))

