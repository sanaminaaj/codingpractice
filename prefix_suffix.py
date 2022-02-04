x="acaac" #01234
mid=len(x)//2 #2
i=0
j=len(x)//2
string=""
while i<mid:
    if x[i]==x[j+1]:
        string=string+x[i]
        i=i+1
        j=j+1
    else:
        break
print(string)