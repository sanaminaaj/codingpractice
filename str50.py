s="welcome to python coding"
x='$'
n=5
o=s[0]
for i in range(1,len(s)):
    if (i)%n==0:
        o=o+x
    else:
        o=o+s[i]
print(o)
        