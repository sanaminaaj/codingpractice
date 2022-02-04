n=int(input(""))
f=False
for i in range(1,10):
    for j in range(1,10):
        if i*j==n:
            f=True
            break
if f==True:
    print("yes")
else:
    print("no")