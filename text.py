import textwrap
s="Hello world"
size=3
s=s.split(" ")
for i in s:
    print(textwrap.fill(i,3))
    