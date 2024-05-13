#functions
#block of code =>  jis ko reuse kr sakte hai
'''
def func():
    statement
    '''
def msg(x):#x=>parameter
    print("HEllo",x)

msg("parul")#"parul"=>argunment    
msg(1000)

def msg(x,y): #call by reference
     print("HEllo",x,y)
     return x+y #without return is will give none 
#return k baad functiion k bhar ,return k baad  ka kuch nhi chal ta 
#msg("parul","manan") 
print(msg(10,20))


def fun(x):
        x=x+5

x=10
print(x)
print(id(x))
fun(x)
print(x)#same same 10 coz imutable memo add change
print (id(x))

def fun(x):
    x[0]="aman"
mylist=[10,20]
print(id(mylist))
fun(mylist)
print(mylist)
print(id(mylist))

#function=>3 parameter if 1 > exelent 2> good 3>avg
def marks(x,y,z):
    if(x>y and x>z):
        return "execlent"
    elif(y>x and y>z):
        return "good"
    else:
        return"avg"
marks(10,20,61)    
    
#lcm of 2 no => 2,8 


def grtno(x,y):
  
    if (y>x):
        greatest=y
    else:
        greatest=x
    while i in range (true): 
        if (greatest%x==0 and greatest%y==0 ):
            print("lcm is:",greatest)
        else:
            greatest+1
            
grtno(3,21)            
            
#type of argunment
def employee(eid,ename,email):
    print(f"eid is{eid}/n ename is{ename}/n email is{email}")
    
employee(16,"parul","parul30504@gmail.com")#required argunment=>jite no of peremeter hai ute  arg he chiye 

def employee(eid,ename,email):
    print(f"eid is{eid}/n ename is{ename}/n email is{email}")
    
employee(16,"parul30504@gmail.com","parul")#positional argunment jis sequence mai para.diya hai us seq mai arg bhi do

def employee(eid,ename,email):
    print(f"eid is{eid} ename is{ename} email is{email}")
    
employee(eid=16,email="parul30504@gmail.com",ename="parul")#keyword argunment by give key word..

def employee(eid,ename,email):
    print(f"eid is{eid}\n ename is{ename}\n email is{email}")
    
employee(16,email="parul30504@gmail.com",ename="parul")#mix of positional and keyword

def employee(eid,ename,email="sjkdhfksj"):
    print(f"eid is{eid} ename is{ename} email is{email}")#default arg
    
employee(16,"parul")
employee(16,"parul","parul30504@gmail.com")#replaced with default

#variable length argunment(args)  #what is the difference between args and kwargs
#cant identify on which index wht value
def facebook(*data):
    print(data,type(data))#tuple
facebook(10,20,65,"parul")    

#keyword variable length argunment(kwargs)
def facebook(**data):
    print(data,type(data))#dict
facebook(username="parul",age=20)

def fun():
    print("hello")

x=fun
print(fun)
print(x)
x()


#high order function
#which take another function as an argunment
def sq(x):
    print(x*x)
    
print(sq(10)) #100 none   

def add(x,fun):
    print(x,fun)
    
print(10,20)  #10,20

def add(x,fun):
    print(x,fun)
    
print(10,sq(5)) 

def add(x,fun):
    return x*x
    
print(10,20)  #10,20

def add(x,fun):
    print(x,fun)
    
print(10,sq )

def sq(x):
    return x*x
    

def add(x,fun):
    print(x,fun(3))
    
print(10,sq)#10,9

name=["parul","purva","pri","chinku"]
myname=[x for x in name if "a" in x]
print(myname)#list comprihension
 
