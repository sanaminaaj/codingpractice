def gcd(a,b):
    while True:
        if a<b:
            b=b-a
        elif a>b:
            a=a-b
        else:
            return a
print(gcd(978,895489))