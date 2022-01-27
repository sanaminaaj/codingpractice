'''A = "aabcd"
B = 2
out:bcd
Input 2:
A = "aabbccd"
B = 2
out:d
'''
def consecutive():
    A = "aabbccd"
    B = 2
    out=""
    for i in range(0,len(A),B):#5: B-2
        s=A[i:i+B]
        if s!=s[::-1] or len(s)==1:
            out=out+s
       
    print(out)
consecutive()
            
            
        
        

