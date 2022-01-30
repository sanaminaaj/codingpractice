l=[1,2,3,4,5]
def minimum(l,i,j):
    mini=l[i:j+1]
    return min(mini)
print(minimum(l,0,4))
print(minimum(l,1,3))