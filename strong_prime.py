def prime(x):
    list_of_prime=[]
    for i in range(2,x+1):
        c=0
        k=i
        for j in range(1,i+1):
            if k%j==0:
                c=c+1
        if c==2:
            list_of_prime.append(j)
    return list_of_prime
def strongprime(i,j):
    l=prime(350)
    for i in range(1,len(l)-1):
        if (2*l[i])>l[i-1]+l[i+1]:
            print(l[i]) 
strongprime(2,350) 
    