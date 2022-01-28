x,y,op,z=input("").split(" ")
sum1=0
x=int(x)
y=int(y)
z=int(z)
for i in range(x,y+1):
    if op=='+':
        sum1=sum1+(i+z)
    elif op=='-':
        sum1=sum1+(i-z)
    elif op=='*':
        sum1=sum1+(i*z)
    else:
        sum1=sum1+(i/z)
print(sum1)
    