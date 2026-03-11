'''
Globalstar={"Akhil","Kaushik","Bhavanisai","John","pookesh","josh","hithesh"}
Alubhai={"vigu","faa","chal chal","nachi"}
print(Globalstar | Alubhai)
print(Globalstar.union(Alubhai))
print()
print(Globalstar.intersection(Alubhai))
print(Globalstar & Alubhai)

print()

print(Alubhai-Globalstar)
print()

print(Globalstar.symmetric_difference(Alubhai))
print(Alubhai^Globalstar)

print()

print(Globalstar.issubset(Alubhai))
print(Alubhai.issubset(Globalstar))
print(Globalstar<=Alubhai)
'''
x={1,2,3}
y={3,4,5,6,1,2}
print(x.isdisjoint(y))
print(x>=y)

print(y>=x)

print(x<=y)