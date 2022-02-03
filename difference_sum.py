s=str(1453)
odd=0
even=0
for i in range(len(s)):
    if i%2==0:
        even=even+int(s[i])
    else:
        odd=odd+int(s[i])
print(abs(even-odd))
        
