x=["python","java","codegnan","gnan"]
l=[]
for i in x:
    l.append(i[0].upper()+i[1:])
print(l)


print(list(map(lambda x:x[0].upper()+x[1:],x)))

print(list(map(lambda x:x if len(x)>4 else "False",x)))


x=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2!=0,x)))