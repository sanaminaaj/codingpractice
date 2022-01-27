l=[1,2,2,3,1,4,5]
o=[]
for i  in range(len(l)):
    if l.count(i)==1 and i not in o:
        o.append(i)
print(o)
        