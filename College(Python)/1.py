def fun():
    lst={1,2,3}
    sum=0
    for i in lst:
        sum=sum+i
        

    return sum
x,y=("The sum of all the number in a list is",fun())
print(x,y)