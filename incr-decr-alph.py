n=10
for i in range(n):
    print(" "*(n-i),end="")
    j=1
    for k in range(i+1):
        print(j,end="")
        j=j+1
    j=i+65
    while j>65 :
        print(chr(j),end="")
        j=j-1