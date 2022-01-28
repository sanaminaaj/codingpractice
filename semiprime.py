'''semiprime'''
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
def semiprime(n):
    list=prime(n)
    for x in range(n):
        a=x
        for y in range(len(list)):
            b=list[y]
            for z in range(y+1,len(list)):
                c=list[z]
                if b*c==a:
                    print(b,c,"=",a)
            
semiprime(50)           
                