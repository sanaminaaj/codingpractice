s="hello1welcome2@python:5:2:3"
k=""
out=""
numbers=[]
'''a:b:c
a=right
b=left
c=remove letters at c position"
'''
for i in s:
    if i!=':':
        k=k+i
    else:
        break
numbers.append(s[-5])
numbers.append(s[-3])
numbers.append(s[-1])
t=int(numbers[0])-int(numbers[1])
n=-1*t
out=out+k[n:]+k[:len(k)-t]
print(out)
output=""
index=int(numbers[2])
print("index:",index)
for i in range(len(out)):
    if i%index==0:
        pass
    else:
        output=output+out[i]
print(output)
    