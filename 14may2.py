#(0°C × 9/5) + 32 (c to f)
Amount = [21,23,18,22,19,34,24,35]
a=list(map(lambda x : x*(9/5),Amount))
print(a)

#(sequence is 25 to 40)
x=[25, 28,26,4000,27, 31, 5,28,29,30,34,8,32,33, 35, 32,37,36, 40,38,39, 95]
b=list(map(lambda x: x if 25<=x<=45 else False ,x))
print(b)

#duplicate 
List =[3,5,2,6,8,3,18,5,3,44,21,4,18,2]
x=[]
for i in List:
    if(i not in x):
        x.append(i)
print (x)      

  


n=[]
for x in n:
    val=(int(input("enter")))
    if x not in n:
        n.append(val)
print (n)        

# palandrom
def palandrom(x):
    return x == x[::-1]

x=(input("enter"))
if palandrom(x):
    print("yes")
else:
    print("no")
       