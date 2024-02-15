"""
选数
"""

from math import *
from itertools import *


def is_prime(n):
    if n == 1:
        return False
    m = int(sqrt(n) + 1)
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


n, k = map(int, input().split())
s = list(map(int, input().split()))
cnt = 0
for e in combinations(s, k):  # 所有组合
    num = sum(e)  # 求和
    if is_prime(num) == True:
        cnt += 1
print(cnt)
