'''
l= []

for i in range(1, 101):
    if i % 2 == 0:          # condition to check even
        l.append(i)

print(l)
'''
'''
l=["a","b","c","d","e"]
for i in range(len(l)):
    l[i]=l[i].upper()
print(l)
'''
l=["a","b","c","d","e"]
for i in range(len(l)):
    l[i]=l[i].upper()
print("".join(l))