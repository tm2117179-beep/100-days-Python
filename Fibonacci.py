n=int(input("Enter the numebr: "))
if(n<=0):
    print("There is no output for that value")
a=0
b=1
if(n>0):
    print(a)
if(n>1):
    print(b)    
count=0
while(count<n-2):
    nextnumber=a+b
    print(nextnumber)
    a=b
    b=nextnumber
    count=count+1
