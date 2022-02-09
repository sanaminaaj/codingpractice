s="hackthegame"
d={}
for i in s:
    d[i]=s.count(i)
    
for i in range(len(s)):
    if d[s[i]]==1:
        print(i+1)
        break