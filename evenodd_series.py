s="%#32%#%2"
o=[]
for i in s:
    if i.isdigit():
        o.append(int(i))
l=list(set(o))
l.sort(reverse=True)
print(l)
def string(x):
    s=""
    for i in x:
        s=s+str(i)
    return s
if o[-1]%2==0:
    print(string(o))