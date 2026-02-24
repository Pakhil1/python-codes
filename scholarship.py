#scholarship student marks py java math stat add is more than 350 and age should be less than 18
py=int(input("Enter marks:"))
java=int(input("Enter marks:"))
math=int(input("Enter marks:"))
stat=int(input("Enter marks:"))
age=int(input("Enter age of student: "))
total=py+java+math+stat
if total> 350 and age < 18:
    print(" Student is eligible for the scholarship")
else:
    print(" Student is not eligible for the scholarship")
    print("Total Marks:")

