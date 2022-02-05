def total_string_pair(x,y):
    x=set(x)
    y=set(y)
    if x.issubset(y) or y.issubset(x):
        return True
    else:
        return False
a=["abc","def","smpabc","jhi","jhrti","definition"]
#a=["similar","ground","heaven","hell","earth","liar","shelf"]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        t=total_string_pair(a[i],a[j])
        if t:
            count=count+1
print(count)      