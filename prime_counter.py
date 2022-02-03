n=30
c=0
def cp(x):
    count=0
    for i in range(2,x+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            count=count+1
    return count
def prime(x):
    count=0
    c=0
    for j in range(1,i+1):
        if x%j==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
for i in range(1,n):
    x=cp(i)
    print(i,":",x)
    if prime(x):
        c=c+1
print(c)
        