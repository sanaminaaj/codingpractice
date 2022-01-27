def isharshad(s):
    sum1=sum_of_digit(s)
    if s%sum1==0:
        print("harshad")
    else:
        print("not")
def sum_of_digit(s):
    sum1=0
    while s>0:
        r=s%10
        sum1=sum1+r
        s=s//10
    return sum1
isharshad(156)
        