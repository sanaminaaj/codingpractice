s="welcome to python coding"
check_list=["to","coding"]
out={}
for i in check_list:
    l=[]
    f=s.find(i)
    l.append(f)
    l.append(f+len(i)-1)
    out[i]=l
print(out)
    
