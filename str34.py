s="geeksforgeeks"
d={}
for i in s:
    d[i]=s.count(i)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        d[s[i]]-=1
print(d)
    