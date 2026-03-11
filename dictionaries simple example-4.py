b=["AKhil","kaushik","Bhavanisai","john"]
d={}
for i  in b:
    word=len(i)
    if word not in d:
        d[word]=[i]
    else:
        d[word]+=[i]
print(d)        
        
'''        
for i in b:
    d.setdefault(len(i),[]).append(i)
print(d)
'''        