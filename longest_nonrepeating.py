s="A@bcd1abx"
s=s.lower()
o=""
temp=""
for i in s:
    if i not in o:
        o=o+i
    elif len(o)>len(temp):
        temp=o
        o=""+i
print(len(temp))