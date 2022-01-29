s="mango apple papaya orange plums banana"
s=s.split(" ")
c=0
w=""
for i in s:
    if len(i)>c:
        c=len(i)
        w=i
print(w)