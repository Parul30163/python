#polymorphism>> many form.
#variable, operation,object
#method over ridding
#operator overloading
1+2

"1"+"2"

class vhec:
    def info(self):
        print("kjenf")
class tata(vhec):
    def t(self):
        print("jHsdnjenf")
'''c1=vhec()
c1.info()

t1=tata()
t1.t()'''

t1=tata()
t1.info()


class employee:
    def __init__(self,num1):
        self.num1=num1
    def __repr__(self):#representation mai kam aata hai
        return f"hey{self.num1}"
    def __add__(x,y):
        print("hello",x.num1,y.num1)
    
e1=employee(10)
print(e1)
e2=employee(30)
print(e2)

e1+e2
 

#2 class (x,y) gt
class add:
    def __init__ (self,num1,num2):
        self.num1=num1
        self.num2=num2   
    
    def __gt__(self,obj2):
        if (self.num1+self.num2>obj2.num1):
            return False
        else:
            return True
        
n1=add(5,4)
n2=add(6,8)
n1>n2

        
#procted variable>>use vo kare ga jo class inherat kr re hai

class parent:
    _amount=100 ## _>>protected >>only for show
    
#privat
class parent:
    __amount=100 ## __ >>private>>>_CLass__xyz
class son(parent):
    salary=10
p1=parent()
p1._parent__amount
# their no such thing  as modifier in python..>>privat public default protected ...only shown>>encaptilauction        