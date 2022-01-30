l=[0,1,1,0,1,1,0,0]
#[0,0,0,1,1,1]
o=[]
for i in l:
    if l[i]==0:
        o.append(0)
size_one=len(l)-len(o)
for i in range(size_one):
    o.append(1)
print(o)
        
