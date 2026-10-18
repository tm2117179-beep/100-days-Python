# di={'a':4,'b':5,'c':6}
# d={di[i]:i for i in di}
# print(d)


di={'a':4,'b':5,'c':6}
d={}
for i in di:
    d.update({di[i]:i})

print(d)