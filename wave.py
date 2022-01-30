l=[1,2,3,4,5,6,7,8]
#o=[2,1,4,3,6,5]
l.sort()
#[6,5,4,3,2,1]
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
    