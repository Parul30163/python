#lambda function=>annoymous function
#nam3(gumnam)
#lambda se start
def fun(x):#same parameter
        return x+1
    
lambda x: x+1

def fun(x):#same parameter
        return x+10
x=fun
x(5)

out =lambda x: x+10#used with high order fun
out(5)

#map,filter,reduce
#map(fun, iterable<list\str..>)
def squre(x):
    return x*x
#..............
mylist=[10,20,30,40,11]

list(map(squre,mylist))



list(map(lambda x: x*x, mylist))

list(filter (lambda x: x%2!=0, mylist))


#file handling (how to perform read or write)
#open(file, access_mode)
#read\write
#close

fileobj=open("14maytxtfile","r+")#path # fileobj>variable obj
x=fileobj.read()
fileobj.write("manan")
fileobj.close()

print(x)


fileobj=open("14maytxtfile","r")#path # fileobj>variable obj
x=fileobj.read()

fileobj.close() #only read (r)
print(x)

fileobj=open("14maytxtfile","r+")#path # fileobj>variable obj
x=fileobj.read()
fileobj.write("manan hello")#read and write(r+)
fileobj.close()

print(x)

fileobj=open("14maytxtfile","w+")#purana content hat jaa agha or new aaja agha(w+)
x=fileobj.read()
fileobj.write("manan hello")
fileobj.close()

print(x)


#change the position of coursor
fileobj=open("14maytxtfile","w+")#purana content hat jaa agha or new aaja agha(w+)
print( fileobj.tell())#
fileobj.seek(2)#change the position of corsur
x=fileobj.read()
fileobj.write("manan hello")
print( fileobj.tell())
fileobj.close()

print(x)


# read file with "with" keyword
with open("14maytxtfile","r") as fileobj: #path # fileobj>variable obj
    x=fileobj.read()
 
    print(x)
    


#read line one by one

with open("14maytxtfile","r") as fileobj: #path # fileobj>variable obj
         print(fileobj.readline())
         print(fileobj.readline())
         print(fileobj.readline()) # line one by one
    
 
 
    
with open("14maytxtfile","r") as fileobj: #path # fileobj>variable obj
             for line in fileobj.readlines():
                print (line.strip())
         
  
with open("14maytxtfile","r") as fileobj: #path # fileobj>variable obj
             for line in fileobj.readlines():
                print (line)
                          
 

import csv
fileobj= open("14maytxtfile","r")  #path # fileobj>variable obj
f=csv.reader(fileobj) 
for i in f:
    print(i)
    id,name,salary=i
    
    
import csv
fileobj= open("14maytxtfile","r")  #path # fileobj>variable obj
f=csv.reader(fileobj) 
for i in f:
   
    id,name,salary=i
    print(id,name, salary)
    
    
#exception handling 
#unwanted  error
#try   except:
try:
    print("hello")
    x=10
    x/0
    print("hey")
    
except:
    print("error handling")    
    
    
                                      
try:
    print("hello")
    x=10
    x/0#error
    print("hey")
    
except (ZeroDivisionError,NameError ) as z :
    print("error handling: ", z)    
    
    
    
try:
    print("hello")
    x=10
    x/num#error
    print("hey")
    
except (ZeroDivisionError,NameError ) as z :
    print("error handling: ", z) 
    
    
    
try:
    print("hello")
    x="parul"
    x[10]
    print("hey")
    
except (ZeroDivisionError,NameError ) as z :
    print("error handling: ", z) 
except Exception as e:
    print(e)#all the error
    
    
    
#only syntax error cant be handel by exception handling

try:
    print("hello")
    x="parul"
    try:  #nested
    
        x[10]
    except:
        
        print("hey")
    
except (ZeroDivisionError,NameError ) as z :
    print("error handling: ", z) 
except Exception as e:
    print(e)#all the error
    
    
try:
    print("hello")
    x=10
    x/1    
    print("hey")
    
except Exception as e:
    print(e)#all the error
else:
    print("dmbc")
    
    
    
try:
    print("hello")
    x=10
    x/1    
    print("hey")
    
except Exception as e:
    print(e)#all the error
    
finally:#challl aa ghaa heeee errror ho n ho
    print("dmbc")
    
    
    
                                                             