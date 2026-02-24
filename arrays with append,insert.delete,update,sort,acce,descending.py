#array operation append,delete,insert,sorting,ascending,descending,update
arr=[10,20,30,40,50]
print("lenght of array:",len(arr))
arr.append(90)
print("array after append:",arr)
arr.insert(5,25)
print("array after inserting:",arr)
arr.remove(30)
print("array after deleting:",arr)
arr.sort()
print("array after sorting:",arr)
arr.sort(reverse=True)
print("array after sorting in descending order:",arr)
new_arr=sorted(arr)
print("new sorted array:",new_arr)
new_arr[5]=60
print("array after updating:",new_arr)
