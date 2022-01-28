def div(n,a):
    s=0
    while s!=1:
        s=n/a
    return s
    
n=5
result=n
while result!=1:
    result=div(result,2)
while result!=1:
    result=div(result,3)
while result!=1:
    result=div(result,5)       
        
if result==1:
    print(n)