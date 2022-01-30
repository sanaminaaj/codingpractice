def n_thprime(n):
    i=0
    l=[]#2,3
    while i<n:
        for m in range(2,2*n+1):
            k=m
            c=0
            for j in range(1,m+1):
                if k%j==0:
                    c=c+1
            if c==2:
                l.append(k)
                i=i+1
    return l[n-1]
print(n_thprime(204))
                    
                    
                        