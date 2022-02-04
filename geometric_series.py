from math import ceil
n=int(input(""))
if n%2==0:
    s=(n//2)-1
    print(3**s)
else:
   s=ceil(n//2)
   print(2**s)