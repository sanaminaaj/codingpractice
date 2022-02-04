n="1A"
sum1=0
d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
l=len(n)-1
for i in n:
    if i.isalpha():
        s=i.upper()
        sum1=sum1+d[s]*(17**l)
        l=l-1
    else:
        sum1=sum1+int(i)*(17**l)
        l=l-1
print(sum1)