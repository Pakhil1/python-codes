'''
x=["python","java","bava","cython"]
for i in range(len(x)):
    x[i]=x[i][0].upper()+x[i][1:]
print(x)    
'''
#
x=["python","java","java","python"]
i=0
while i < len(x):
    x[i] = x[i][0].upper() + x[i][1:]
    i += 1
print(x)
