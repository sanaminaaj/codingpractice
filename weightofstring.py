d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
vowel_weight=1
sum1=0
s="all zebras are  black & white"
s=s.lower()
if vowel_weight==1:
    for i in s:
        if i in d:
            print(d[i],end="  ")
            sum1=sum1+d[i]
else:
    for i in s:
        if i in ['a','e','i','o','u']:
            sum1=sum1+0
        elif i in d:
            print(d[i],end="  ")
            sum1=sum1+d[i]
        
print(sum1)