print("hello",end="-")
print("hi alien")
age=100
print(type(age
        ))
city="parul"
print(type(city))
address="""4/216 old
housing 
board """

#multiline string
company= "regex"
year=2024
print("company name:",company,"year is",year)#company is variable
company= "regex"
year=2024
print(f"company name:{company} year is{year}")#string formating f...{}
username= "parul"
msg=f"ierhfjkh{username}"
print(msg)
username="manan"
print(msg)
city="hi"
print("before",id(city))#same
y="hi"
print("before",id(y))#same
city="yo"
print("before",id(city))
#if we make any varialbe and we change it and make new memory add so imutable,if it doent make new memory then then it is mutable
print(y)
print (city)
#operators
#arthematic
20/3#divide...ans float
#floor division....int
20//3
10.0+5 # ans in float coz 10.0>5
1+5*4/2-7+8# ans floatt / 
# % reminder
23%3
#**
2**3
3**4
#arth. precendence rule
# **
#* / // %
#+ -

#assignmentop
x=10
x+5
print(x)
x+=5
print(x)
#+= -= *= /= 
#coompresion >= <= ==
#logical  and or not
x=10
y=19
x==10 and y>18
#membership and identity op

"j" in "jaipur" #membership  {case sensitive}
"purj" in "jaipur"
"x" not in "jaipur"
#identity op
#varible belong to certain datatype or object  belong to a class
x=10
type(x) is int
type(x) is not int
# == and is op
x=500
y=500
x==y # check data
x is y # memory add check
#0-255 fix memory add hoti hai..
# 256.... se new memmory add banta hai
#conditional statenment
#if statenment
x=10
if(x==10):
    print("jnfk")
    x=int(input("enterno:"))
if(x>=60):
    print("avg")
elif(x>75 and x<80 ):
    print("good")
elif(x>80):
    print("exelent")    
else: 
     print("bad")
        
a=10
b=90
c=4
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else: 
     print(c)
        
        
