# assignment 1

#create an array using numpy
import numpy as np
x=int(input("enter len"))
ls=[]
for i in range(x):
    a=int(input("enter value in list: "))
    ls.append(a)
b=np.array(ls)
b

#create an array of random 10 integer
import numpy as np
a=np.random.randint(1,100,10)
a

#create an array of element 10-20
import numpy as np
ls=[]
for i in range(10,21):
    ls.append(i)
    
b=np.array(ls)
print(b)

#create an array which contain value 5,10 times
import numpy as np
ls=[]
val=[5]*10
ls.append(val)
    
b=np.array(ls)
b

#create a 1D array and convert it into 3x3matrix
import numpy as np
a=np.random.randint(1,100,9)
a


b=np.array(a).reshape(3,3)
b

#create a 2D array of 3x3 matrix elenment between 0 to 1
import numpy as np
a=np.random.rand(9)
a

b=np.array(a).reshape(3,3)
b

#conc 2D array hstack and vstack
import numpy as np
a=np.array([5, 9, 6])
b=np.array([8, 2, 7])
a

b

np.hstack((a,b))


np.vstack((a,b))

