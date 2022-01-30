l=[[1,2,3],[4,5,6],[1,2,3]]
for i in range(3):
    k=i
    n=0
    for j in range(i+1):
            print(l[n][k],end=" ")
            k=k-1
            n=n+1
    print()
k=len(l)-2
n=len(l)-1
while k<=len(l)-1:
    print(l[k][n],end=" ")
    k=k+1
    n=n-1
print()
print(l[len(l)-1][len(l)-1])
    