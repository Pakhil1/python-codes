#write a code to part a right angledd triangle pattern of numbers using nested loops

#write a given number of rows
n=int(input("Enter the number of row:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')#replace "*" with i/j to print numbers instead of stars
    print()    
    
    
