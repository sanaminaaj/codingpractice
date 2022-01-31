s="codeecode"
i=0
j=len(s)-1
c=""
mid=(i+j)//2
while mid>=0:
    if s[mid]==s[j]:
        c=c+s[mid]
        mid=mid-1
    else:
        mid=mid-1
print(c)