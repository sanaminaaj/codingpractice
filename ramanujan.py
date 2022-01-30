import math
n=1729
d={}
cube=math.floor(n**(1/3))
for i in range(cube+1):
    a=i
    for j in range(cube+1):
        b=j
        if a**3+j**3==n:
            d[a]=b
print(d)
            