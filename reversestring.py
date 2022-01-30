inp="Hello 123 World"#01234567
out=""
j=len(inp)-1
inp=inp.split(" ")
for i in inp:
    if i.isalpha():
        out=out+i[::-1]+" "
    elif not i.isalpha():
        out=out+i+" "
print(out)


        