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
    return l
def semiprimecheck(n):
    list=prime(n)
    f=False
    for i in range(len(list)):
        x=list[i]
        for j in range(i,len(list)):
            y=list[j]
            if x*y==n:
                f=True
                print("semiprime")
    if f==False:
        print("not semiprime")
semiprimecheck(57)