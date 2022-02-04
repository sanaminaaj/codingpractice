s="sanam"
length=len(s)//2
s=s[length:]+s[:length+1]
for i in range(len(s)-1):
    for j in range(i+1):
        print(s[j],end="")
    print()