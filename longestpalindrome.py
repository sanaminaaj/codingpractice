str="moomso"
l=[]
for i in range(len(str)):
    for j in range(len(str)):
        if str[i:j+1]!="":
            l.append(str[i:j+1])
def pal(n):
    n=str(n)
    if n==n[::-1]:
        return len(n)
for i in range(len(l)):
    long_palindrome_length=0
    if pal(l[i])>long_palindrome_length:
        long_palindrome_length=pal(l[i])
print(long_palindrome_length)
    
    