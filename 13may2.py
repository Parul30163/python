#assignment day2
'''def generate_n_chr():
    for i in range(x):
        print(y,end="")

x=int(input("enter no."))
y=str(input("enter alph.."))
generate_n_chr()#output= ppppp

#max no from list
def max_in_list(x):
    max_value= x[0]
    
    for i in x[1:]:
        if (i> max_value):
            max_value=i
    return max_value

x=[10,20,85,62]
print(max_in_list(x))#output=> 85


#length of string
def word_len(lst):
    length=[]
    for i in lst:
        length.append(len(i))
    return length

word=["manan","chinku","parul"]
length= word_len(word)
print(length)#output=> [5,6,5]

#longest word length
def lword_length(lst):
    max_length=0
    for word in lst:
        if  len(word)> max_length:-
            max_length=len(word)
    return max_length    
word=["manan","chinku","parul"]
print(lword_length(word))#output=> 6 


#LAMBDA FUNCTION
ls = lambda word_list: max(len(word) for word in word_list)
words = ["parul","manan","chinku"]
print( ls(words))

#integer n length word
x=["parul","manan","chinku","parthivi","priyani"]
n=int(input("enterno: "))
y=[]
for i in x:
    if (len(i)>=n):
        y.append(i)
print(y)
#using filter 
x=["parul","manan","chinku","parthivi","priyanijersgs"]
n=int(input("enterno: "))
print(list(filter (lambda a: len(a)>=n, x)))

def pangram(x):
    if (x in "zxcvbnmasdfghjklqwertyuiop"):
        return True
    else :
        return False
    
x="The quick brown fox jumps over the lazy dog"
for i in x:
    print(pangram(i))    
 
 #translator()   
def translator(n):
    print(dic[n]) 
dic={"merry":"god","christmas":"jul", "and":"och", "happy": "gott", "new":"nytt", "year":"år"}
n=str(input("enter english word"))
translator(n)


# find repetation of letter
def repet(x):
        c={}
        for i in x: 
                if(i in c ):
                    c[i]+=1
                else:
                    c[i]=1             
        print (i,c) 
       
x="abbabcbdbabdbdbabababcbcbab"
repet(x)
'''

def mathamatic_py (op,a,b):
        if (op=='+'):
            c=a+b
            print(c)
        elif(op=='-'):
            d=a-b
            print(d)
            
        elif(op=="max"):
            if (a>b):
                print(a)
            else :
                print(b) 
        elif(op=="min"):
            if (a<b):
                print(a)
            else :
                print(b) 
                
mathamatic_py ('+',5,8)                               
mathamatic_py ('-',5,8)                         
mathamatic_py ('max',5,8)             
mathamatic_py ('min',5,8)             
                        



















