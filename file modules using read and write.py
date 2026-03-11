file =open("akhil.txt",mode="r+")
name=input()
age=int(input())
marks=float(input())
file.write("f{name:<15}{age:^20}{marks:>15}\n")
file.write(f"{name}{age}{marks}\n")
print("completed")
file.close()

