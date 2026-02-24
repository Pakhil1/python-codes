'''
a=["john","kaushik","Bhavanisai","Akhil"]
for i in range(len(a)-1,-1,-1):
    print(a[i])
  '''

l=["a","b","c","d","e"]
for i in range(len(l)):
    if i%2==0:
        l[i]=l[i].upper()
    else:
        l[i]=l[i].lower()
        
print("".join(l))        
 