def factors(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
n=12
if factors(n)>n:
    print("abundant number")
else:
    print("not abundant number")
            