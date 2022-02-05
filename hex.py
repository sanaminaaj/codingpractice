a="1A"
b=26
d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
o=0
po=len(a)-1
for i in a:
    if i.isdigit():
        o=o+int(i)*(16**po)
        po=po-1
    else:
        temp=d[i]
        o=o+temp*(16**po)
        po=po-1
print(o)
if o==b:
    print("equal")
else:
    print("not")
        