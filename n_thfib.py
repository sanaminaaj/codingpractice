def n_thfib(n):
    i=0
    l=[]
    f0=0
    f1=1
    l.append(f0)
    l.append(f1)
    while i<n:
        f2=f0+f1
        l.append(f2)
        f0=f1
        f1=f2
        i=i+1
    print(l[n-1])
n_thfib(10)