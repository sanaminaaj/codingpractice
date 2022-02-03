n=3
list1=list(map(int,input().split(" ")))
length=len(list1)
l1=list1[:(length//2)+1]
l2=list1[(length//2):]
output=[]
for i in range(len(l1)-1):
    sum1=l1[i]+l2[i]
    output.append(sum1)
print(output)