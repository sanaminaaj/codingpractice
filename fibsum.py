n=10
l=[]
def fibsum():
    i=0
    l.append(0)
    l.append(1)
    f0=0
    f1=1
    f2=f0+f1
    while f2<n:
        l.append(f2)
        f0=f1
        f1=f2
        f2=f0+f1
    l.append(f2)
    return sum(l)
print(fibsum())
        
        