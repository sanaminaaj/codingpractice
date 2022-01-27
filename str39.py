# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input(""))
l=input("").split(" ")
def positive():
    f=True
    for i in range(len(l)):
        if not int(l[i])>0:
            f=False
    return f
s=str(n)
def pal():
    if s==s[::-1]:
        return True
    else:
        return False
if positive() and pal():    
    print(True)
else:
    print(False)
         