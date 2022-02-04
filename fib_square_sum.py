n=9
def fib():
    f=[]
    f1=1
    f2=1
    f3=f1+f2
    i=0
    f.append(f1)
    f.append(f2)
    f.append(f3)
    while i<n-3:
        f1=f2
        f2=f3
        f3=f1+f2
        f.append(f3)
        i=i+1
    print(f)
    return f
def square_fib(f):
    sum1=0
    for i in f:
        sum1=sum1+(i*i)
    return sum1
f=fib()
print(square_fib(f))
    
    
    