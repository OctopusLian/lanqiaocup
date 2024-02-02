import os
import sys

# 请在此输入您的代码
res = 0
for i in range(1,13):
    for j in range (1,32):
        s = '2022%02d%02d'% (i,j)
        if'012' in s or '123' in s:
            res +=1
print(res)