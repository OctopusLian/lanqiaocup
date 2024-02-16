"""
等差数列
"""

from math import *

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = 0
for i in range(1, n):
    d = gcd(d, a[i] - a[i - 1])
if d == 0:
    print(n)
else:
    print((a[-1] - a[0]) // d + 1)
