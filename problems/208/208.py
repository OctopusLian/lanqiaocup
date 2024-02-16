"""
带分数
"""

from itertools import *

n = int(input())
bit = len(str(n))  # n的位数
cnt = 0
for num in permutations("123456789"):
    a, b, c = 0, 0, 0
    for al in range(bit):  # al: a的位数，a肯定比n短
        a = int("".join(num[:al + 1]))  # 一个a
        bLast = (n - a) * int(num[-1]) % 10  # b的尾数，(n-a)c%10
        if bLast == 0: continue  # b的尾数不可能等于0，因为只用到1~9
        bl = num.index(str(bLast))  # 根据b的尾数，确定b的长度
        if bl <= al or bl >= 8: continue
        b = int("".join(num[al + 1:bl + 1]))
        c = int("".join(num[bl + 1:]))
        if b % c == 0 and n == a + b // c:   cnt += 1
print(cnt)
