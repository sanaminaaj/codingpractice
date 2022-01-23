n=195
k=str(n)
while k!=k[::-1]:
    n=n+int(k[::-1])
    k=str(n)
print(k)