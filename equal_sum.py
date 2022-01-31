from itertools import combinations
l=[-1,1,0,0,2,-2]
sum1,c=0,0
for i in combinations(l,4):
    if sum(i)==sum1:
        print(i)
        c=c+1
print(c)