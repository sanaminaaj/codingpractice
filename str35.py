s="I love to swim and I like to travel abroad"
c=0
d={}
for i in range(len(s)):
    d[s[i]]=s.count(s[i])
for i in d.values():
    if i==1:
        c=c+1
print(c)
    
