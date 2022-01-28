def prime(n):
    l=[]
    for i in range(2,n):
        k=i
        c=0
        for j in range(1,n):
            if k%j==0:
                c=c+1
        if c==2:
            l.append(k)
    print(l)
prime(121)
'''for i in range(2,n):
        k=i
        c=0
        for j in range(1,n):
            if k%j==0:
                c=c+1
        if c==2:
            l.append(k)
    return l'''