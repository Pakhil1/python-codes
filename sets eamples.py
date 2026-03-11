x={0}
print(type(x))
x=set()
print(type(x))

x={1,True,0,False}
print(len(x))
print(max(x))
print(min(x))


s={1,2,3,4,6}
print(s)
s.add(5)
s.add(6)

#update:
s.update([8,9,0])
s.update(("a","b","c"))

s.update("xyz")

s.remove("x")
#s.remove("k")

s.discard("K")

n=s.copy()
print(n)


