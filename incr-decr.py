n=10
for i in range(n):
    print(" "*(n-i),end="")
    j=1
    for k in range(i+1):
        print(j,end="")
        j=j+1
    j=i+1
    while j!=1:
        j=j-1
        print(j,end="")
    print()
    