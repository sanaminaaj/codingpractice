def palindrome(s):
    if s==s[::-1]:
        return True
x=145
if palindrome(str(x)):
    print(len(str(x)))
else:
    x=x+int(str(x)[::-1])
    if palindrome(str(x)):
        print(len(str(x)))
        
    