l=[[4,2,0,6],[3,2,9,7],[1,9,2,0],[3,6,1,4]]
k=[[4,2,0,6],[3,2,9,7],[1,9,2,0],[3,6,1,4]]
def zerorow(x):
    for i in range(len(k)):
        k[x][i]=0
def zerocol(x):
    for i in range(len(k)):
        k[i][x]=0
for i in range(len(l)):
    m=l[i]
    if 0 in m:
        inde=m.index(0)#2
        zerorow(i)#4-2=2
        zerocol(inde)
    
print(k)