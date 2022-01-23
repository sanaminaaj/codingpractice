l=[4,0,2,3,0]
new=[]
count=0
for i in l:
    if i!=0:
        new.append(i)
    else:
        count=count+1
for i in range(count):
    new.append(0)
print(new)