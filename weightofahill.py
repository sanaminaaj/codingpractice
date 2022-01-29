n=4
weight=1
increment=5
sum1=0
for i in range(n):#0,1,2,3,4
    for j in range(i+1):
        sum1=sum1+weight
    weight=weight+increment
print(sum1)