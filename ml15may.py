#intro to Numpy
# why numpy is better then list
#1. same data type> array
#2.memory consum>numpy less , list high
#3.computaion power> numpy high ,list less
#4.function> numpy highr, list less

import numpy as np

a=[1,23,46,63]
type (a)

b=np.array(a)
b

type(b)


x=int(input("enter no"))
n=[]
for i in range (x):
    val=(int(input("enter")))
    n.append(val)
b=np.array(n)
b

#shape=n(rows), n(coulmn)

#size+total_elenment==>n(rows)*n(column)

print("total shape",b.shape)
print("total ele",b.size)

a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)
b

print("total shape",b.shape)
print("total ele",b.size)

#image >pixels >>(0-255)px>> opx(complete black),255px (white)
#convert >>grayscale image>>
#image (pixels)>> normalization(0-1)>> 0px black ,ips (white)

#0,1 >>neorom system (randomization)
 #matrix >>row,column>>
    
#symmatrics matrix>> n(row)=n(column)    
#Asymmatrics matrix>> n(row)!=n(column)
#diagonal elenment =[(1,1),(2,2).....(n,n)]
#zeros().. it will create an array in which all the elenment are zero¶
a=np.zeros(4)
a
b=np.zeros((3,4))
b

#eye()>>it will create array in which digonal elenments are 1 and other are zero
b=np.eye(4)#symmatrix
b

b=np.eye(3,4)#assymertix
b

b=np.eye(10,8)
b

mylist=[10,20,30,40,11]
list(map(lambda x: x*x,mylist))

mylist=[10,20,30,40,11]
list(map(lambda x: x if x%2==0 else False,mylist))

x=lambda a,b,c,d:a+b-c*d
x(3,6,8,9)

mylist=[10,20,30,40,11]
list(filter(lambda x: x%2==0,mylist))

no=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2==0 or x>5,no))


