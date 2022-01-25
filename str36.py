s="7564168"
l=[]
for i in range(len(s)):
    if i%2!=0:
        l.append(int(s[i])*int(s[i]))
print(l)
out=""
for i in range(len(l)):
    out=out+str(l[i])
print(out[:4])