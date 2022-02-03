k=25
bin_k=bin(k).replace('0b','')
consecutive=0
consecutive_zero=0
for i in range(len(bin_k)):
    if bin_k[i]=='0':
        consecutive_zero=consecutive_zero+1
    else:
            consecutive=max(consecutive,consecutive_zero)
            consecutive_zero=0
print(consecutive)
        