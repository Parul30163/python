#loops
#when u no no of time u use for loop otherwise while loop
#string indexing


#position k accordinh
# using (sclicing op)
#[start:stop:[step=1]]
"""state="RAJASTHAN"
state[0:4:1]#raja
state[0:5:2]#rjs
state[0:5:-1]#empty string
state[-1:-4]#empty string
state[-1]
state[-1:-4:-1]

#loops using range
#for i in range(0,10)
#range(start:stop:[step=1])
for i in range(1,5):
    print(i)
for i in range(5,1,-1):
    print(i)
for i in range(1,8,3):
    print(i)    
   

for i in range(97,18,-1):
    
    if (i%5==0 and i%7==0): 
        print(i)   
for i in"helloie":
    print(i)#hello is ittrable
data="helllo"
len(data)

for index in range(0,4):
    print(index,data,data[index])
    
    count=0
for i in "hello":
    count+=1
print(count)  

for y in "hello":
    if(i in "aeiou" ):
        count+=1
print(count)

for y in "hello":
    if(i not in "aeiou" ):
        count+=1
print(count)

#nested loop
for i in range(1,6):
    print("hello",i)
    for j in range(1,5):
        print("parul")
        
        #pattern
for i in range(1,5):
    
    for j in range(1,5):
        print("*",end="")
        
    print("")#change line
    
for i in range(1,6):
    
    for j in range(1,6):
        print(i,end="")
        
    print("")#change line
    
    
for i in range(1,4):
    
    for j in range(1,6):
        print(j,end="")
        
    print("")#change line
    
    
for i in range(1,4):
    
    for j in range(5,0,-1):
        print(j,end="")
        
    print("")#change line
    
for i in range(1,6):
    
    for j in range(1,i):
        print("*",end="")
        
    print("")#change line
    
for i in range(5,0,-1):
    
    for j in range(1,i):
        print("*",end="")
        
    print("")#change line
    
for i in range(1,6):
    for j in range(5,0,-1):   
      for k in range(i,j):
          print("*",end="")
    print("")#change line

for i in range(1,6):
    
    for j in range(i,5):
        print("*",end="")
        
    print("")#change line

for i in range(1,6):   
    for j in range(65,65+i):
        print(chr(j),end="")
        
    print("")#change line
    
for i in range(1,5):
    
    for j in range(1,i+1):
        print(j,end="")
        
    print("")#change line
    
c=1
for i in range(1,5):
    
    for j in range(0,i):
        
        print(c,end=" ")
        c+=1
    print("")#change line
    

a=10
for i in range(1,5):
    
    for j in range(1,i+1):
          
        print(a,end=" ")
        a-=1
    print("")#change line
   
   
c=97
a=1
for i in range(1,5):
    
    for j in range(0,i):
       
        print(a,chr(c),end=" ")
        c+=1
        a+=1
    print()#change line  


    
    
rows = 5

# Loop through each row
for i in range(rows):
    # Print stars for the first column
    print("*", end=" ")
    
    # Print spaces for the columns in between
    for j in range(1, i):
        if i == rows - 1 or j == i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    # Print stars for the last column
    print("*" if i != 0 else "")

a=chr(input("enter password"))"""

#passwordddd questions

password = (input("enter password: "))
valid_symbols ="!@#$%^&*"
upchr=0
for i in range (1,16):
    
    if( 65<= ord(i) <= 90):
        if(upchr<=3):    
           upchr+=1
           print(upchr)
      #prime     
"""no=int(input("entr no:"))
if no>1:
    for i in range(2,no):
        if(no%i==0):
            print(i,"not prime") 
        else:
             print(i,"prime")           
else:
    print(i,"prime")  """
    
    
             
              
           
        
         