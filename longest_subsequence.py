l=[3,10,2,1,20]
m=l[0]
c=1
for i in range(1,len(l)):
    if l[i]>m:
        c=c+1
        m=l[i]
print(c)   