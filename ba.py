s="{([])}[]"
open=[]
for i in range(len(s)):
    if s[i] in ['(','[','{']:
        open.append(s[i])
    elif s[i]==']':
        if open.pop()=='[':
            continue
        else:
            print(i+1)
            open=[]
            break
    elif s[i]==')':
        if open.pop()=='(':
            continue
        else:
            print(i+1)
            open=[]
            break
    elif s[i]=='}':
        if open.pop()=='{':
            continue
        else:
            print(i+1)
            open=[]
            break
if len(open)!=0:
    print(len(s)+1)
else:
    print(0)
    