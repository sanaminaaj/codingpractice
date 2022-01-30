input="hello"
output=[]
l=[]
for i in input:
    l.append(i)
while len(l)!=0:
    e=l.pop()
    output.append(e)
print(output)