"""
最大比例
"""

from math import *


def gcd_sub(a, b):
    if a < b: a, b = b, a
    if b == 1: return a
    return gcd_sub(b, a // b);


n = int(input())
x = list(set(map(int, input().split())))  # set有去重的作用
x.sort()
n = len(x)
a = []
b = []
for i in range(1, n):
    d = gcd(x[i], x[0])
    a.append(x[i] // d)
    b.append(x[0] // d)
n = len(a)
up = a[0]
down = b[0]
for i in range(1, n):
    up = gcd_sub(up, a[i])
    down = gcd_sub(down, b[i])
print('%d/%d' % (up, down))
