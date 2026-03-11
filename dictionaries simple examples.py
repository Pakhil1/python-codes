x={1:"a","a":2}
print(x)
print(x["a"])
print(x.get(2,"element not found"))

print(x.keys())
print(x.values())
print(x.items())

x.update({"Name":"python","language":"eng"})
print(x)

x["name"]="Java"
print(x)
x.pop(1)
print(x)
x.popitem()
print(x)
y=x.copy()
print(y)
x.clear()
print(x)
print(y)
print(x.setdefault("a",999))
print(x)
x.setdefault("b",888)
print(x)