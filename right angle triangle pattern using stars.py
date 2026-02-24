#write a code to print inverted right angle triangle pattern using stars'''
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(i):
        print(j,end=' ')
    print()    
