l=[10,9,4,5,7,2,8,20,21]
sum1=15
s=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        k=[]
        k.append(l[i])
        k.append(l[j])
        if sum(k)%sum1==0 and k not in s:
            s.append(k)
print(len(s))    