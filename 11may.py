for i in range(1,6):
    
    for j in range(i,5):
        print("$",end=" ")
    for k in range(i):
            print("*",end=" ")    
        
    print("")#change line
 
 
 
 
    #while loop
#while(condition)
#for i in range(1,5)
i=1
while(i<5):
    print("hello",i)
    i+=1
    
#list tuple dictionary,set
#list: collection of element ,which has indexd position
#mututable datatype#same memo add mai change hota hai
#orderd collection of elenment
mylist=[10,20,3,0,"parul"]
print(type(mylist))
mylist[0]
mylist[0:15]
mylist[0]=100#update

mylist.append(50)
print(mylist)

mylist.append(50)#(50,100)>error one by one add
print(mylist)

mylist.extend("hey")#ittrable data mang ta hai#multiple data insert
print(mylist)

mylist.extend(["hey",90])#ittrable data mang ta hai#multiple data insert
print(mylist)

help (mylist)

print(mylist)
mylist.pop#delete last elenment
print(mylist)

print(mylist)
mylist.remove("hey")
print(mylist)
del mylist[1]#delete elenment fromposition
print(mylist)


list1=[10,20,60,80,50,"parul"]
for i in list1:
    if (type(i) is int):
        c=i**2
    print(c)
        
        
a=int(input("enter no:"))
total=0
x=a
while(a>0):
        rem=a%10
        total+=rem**3
        a=a//10      
if (total==x):
    print("amstrong")
else:
    print("not amstrong")


#tuple
#fixed no of data
#immutable#new memo adress
#()
#faster then list
mytuple=10,20
print(type(mytuple))
mytuple=(10,20)
print(type(mytuple))
mytuple=(10,)
print(type(mytuple))
#all are above tuple
#....
mytuple=(10)
print(type(mytuple))#int


mytuple=(10,20)
mytuple=mytuple+(60,70)
print(mytuple)


#dictonary
#collection of elenment in form of key:vale
#key is identifire(cant be duplicate),vale is data(can be duplicate)
#orderd collection of elenment{}
mydict={10:'parul',20:'manan'}
mydict[10]#key
mydict[10]='winnie'
print(mydict)
mydict[30]='winnie'
print(mydict)

#delet data(pop(kon sa key pair delet kr na hai),popitem)
x=mydict.pop(10)
print(mydict)
print(x)

x=mydict.pop(20)#delet and return
print(mydict)
print(x)

#"hello"
a={}
for i in "hellooo":
    a[i]=1
print(a)
#key duplicate nhi hoti

100 in a #key check hoti hai(false)
1 in a #false (data/value)

mydict={}
a='aeiou'
b="hey tushar hello"
c=0
for i in "hey tushar hello": 
        if (b in 'aeiou' ):
            
            if i not in mydict:
                mydict[i]=1
        
                        