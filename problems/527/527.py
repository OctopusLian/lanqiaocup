"""
笨小猴
"""

from math import *


def is_prime(n):
    if n == 0 or n == 1:
        return False
    m = int(sqrt(n) + 1)
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


s = input()
maxn = -1
minn = 1000
for i in s:
    n = s.count(i)
    maxn = max(maxn, n)
    minn = min(minn, n)
if is_prime(maxn - minn):
    print("Lucky Word")
    print(maxn - minn)
else:
    print("No Answer")
    print(0)
