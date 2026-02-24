#add a value 10 for each element in an array by traversing through it
#example arr=[1,2,3,4,5]
#output arr=[11,12,13,14,15]
nums=list(map(int,input("Enter elements with  space separation").split()))
for i in nums:
    i+=10
    print(i,end=" ")
