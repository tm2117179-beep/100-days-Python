n=int(input("Enter the numebr: "))
a=0
b=1
print(a)
print(b)
count=0
while(count<n-2):
    nextnumber=a+b
    print(nextnumber)
    a=b
    b=nextnumber
    count=count+1
