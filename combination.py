l=['d','e','H','ILI','oO','r','W']
i=0
j=len(l)-1
out=""
while i<j:
    out=out+l[i]+l[j]
    i=i+1
    j=j-1
else:
    out=out+l[i]
print(out)
    