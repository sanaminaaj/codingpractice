s="geeksforgeeks"
b="geeksgeeksfor"
t=False
for i in range(len(s)//2):
    k=s[2:]+s[0:2]
    s=k
    if k==b:
        print("k:",k)
        t=True
        print("yes")
        break
if t==False:
    print("no")