l=[1,2,4,7]
o=[]
def fact(x):
    if x==1 or x==2:
        return x
    else:
        c=0
        for i in range(1,x):
            if x%i==0:
                c=c+i
        if c in l:
            o.append(c)
for i in l:
    fact(i)
print(o)