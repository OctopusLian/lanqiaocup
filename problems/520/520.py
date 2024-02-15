"""
Hankson的趣味题
"""

from math import *


def lcm(x, y):
    return x // gcd(x, y) * y


n = int(input())
for _ in range(n):
    a0, a1, b0, b1 = map(int, input().split())
    ans = 0
    for x in range(1, int(sqrt(b1)) + 1):
        if b1 % x == 0:
            if gcd(x, a0) == a1 and lcm(x, b0) == b1: ans += 1
            y = b1 // x
            if x == y: continue
            if gcd(y, a0) == a1 and lcm(y, b0) == b1: ans += 1
    print(ans)
