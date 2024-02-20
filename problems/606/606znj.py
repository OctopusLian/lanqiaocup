count = 0
for i in range(1,672):
    for j in range (i+1,1009):
        k = 2019-i-j
        if (k>j and '2' not in str(i)+str(j)+str(k) and '4' not in str(i)+str(j)+str(k)):
            count+=1
print(count)