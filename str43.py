s=["gseeks","geesk","geeksforgeeks"]
minimum=10000
word=""
for i in s:
    if len(i)<minimum:
        minimum=len(i)
        word=i
c=0
for i in range(minimum):
    character=word[i]
    flag=True
    for j in range(len(s)):#3
        if s[j][i]!=character:
            flag=False
            break
    if flag==True:
        c=c+1
    else:
        break
print(c)
            