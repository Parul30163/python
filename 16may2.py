#Q1 Swap the number without using third varible

a=2
b=3
a,b=b,a
print ("a= ",a)
print("b= ",b)

#Q2 : Write a Program to extract each digit from an integer in the reverse order.
a="7536"[::-1]
r =' '.join(a)# saprate it with space using (join) 
m ='@'.join(a)
print(r)
print(m)

#Q3 Write a program that will give you the sum of 3 digits

def sum(x,y,z):
    s=x+y+z
    return s
    
a=int(input("a="))    
b=int(input("b="))
c=int(input("c=")) 

print(sum(a,b,c))

#Q4 Write a program that will take three digits from the user and add the square of each digit.


def sum(x,y,z):
    x=x**2
    y=y**2
    z=z**2
    s=x+y+z
    return s
    
a=int(input("a="))    
b=int(input("b="))
c=int(input("c=")) 

print(sum(a,b,c))

#Q5 Write a program that will check whether the number is armstrong number or not.

a=int(input("enter no:"))
total=0
x=a
while(a>0):
        r=a%10
        total+=r**3
        a=a//10      
if (total==x):
    print("amstrong")
else:
    print("not amstrong")

#Q6 :Write a program that will take user input of (4 digits number) and check whether thenumber is narcissist number or not.

a=int(input("enter no:"))
total=0
x=a
while(a>0):
        r=a%10
        total+=r**4
        a=a//10      
if (total==x):
    print("narcissist")
else:
    print("not narcissist ")    
    
    
#Q7 Display float number with 2 decimal places using print()    
print("{:.2f}".format(10.63556))


#Q8 Print all factors of a given number provided by the user.,4
def factor(x):
    ls=[]
    for i in range(1,x+1):
        if x%i==0:
            ls.append(i)
    return ls    
x=int(input("enter no"))    
print("factor of ",x,"is",factor(x))  

#Q9Accept a list of 5 float numbers as an input from the user          
ls=[]
for i in range(5):
    x=float(input("enter no:"))
    ls.append(x)
    print(ls)
    
#Q10 Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.    
def cy(r,h):
    v=3.14*(r*r)*h
    print(v)
    
r=float(input("r:")) 
h=float(input("h:"))  
cy(r,h) 


