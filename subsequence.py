player_one="STUART"
player_two="KEVIN"
w="BANANA"
l=[]
def subsequence():
    for i
    in range(len(w)+1):
        for j in range(i+1,len(w)+1):
            l.append(w[i:j])
    return l
s=subsequence()
def count(l,word):
    c=0
    for i in l:
        if word==i:
            c=c+1
    return c
p1_score=0
p2_score=0
p2_list=[]
p1_list=[]
for i in s:
    if i[0] in "AEIOU" and i not in p2_list:
        p2_score=p2_score+count(l,i)
        p2_list.append(i)
        #print("p2:",p2_score,"i:",i,"count:",count(l,i))
    if i[0] not in "AEIOU" and i not in p1_list:
        p1_score=p1_score+count(l,i)
        p1_list.append(i)
        #print("p1:",p1_score,"i:",i,"count:",count(l,i))
if p1_score>p2_score:
    print(player_one,"",p1_score)
else:
    print(player_two," ",p2_score)
    
        