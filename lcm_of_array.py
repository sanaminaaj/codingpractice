l=[2,7,3,9,4]
def gcd(a,b):
    while True:
        if a<b:
            b=b-a
        elif a>b:
            a=a-b
        else:
            return a
def mul(l):
    mul=1
    for i in l:
        mul=mul*i
    return mul
a=l[0]
b=l[1]
res=gcd(a,b)
for i in range(2,len(l)):
    res=gcd(res,l[i])
print(mul(l)/res)