names = ["Akhil", "Siva", "Ravi", "Teja", "Kiran"]
marks = [78, 45, 92, 50, 33]
d= {}
for name, mark in zip(names, marks):
    d[name] = mark
for name in sorted(d):
    if d[name] >=50:
        print(name, "got more than 50 marks")