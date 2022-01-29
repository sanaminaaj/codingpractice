n=int(input(""))
n=str(n)
d={}
for i in n:
    d[i]=n.count(i)
c=0
for i,j in d.items():
    if j==1:
        c=c+1
print(c)
        