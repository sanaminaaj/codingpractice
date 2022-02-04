s="coolmadam"
o=""
for i in range(len(s)):
    for j in range(0,len(s)+1):
        m=s[i:j]
        if m==m[::-1] and len(m)>len(o):
            o=m
print(o)
            
            
    