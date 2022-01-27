l=[1,2,5,3,4,7,-4,-3,-1,9]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==0:
            print(l[i],l[j])
