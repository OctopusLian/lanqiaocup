"""
四平方和
"""

from math import *

try:
    n = int(input())
    n_1 = int(sqrt(n))
    for a in range(n_1 + 1):
        n_2 = int(sqrt(n - a * a))
        for b in range(a, n_2 + 1):
            n_3 = int(sqrt(n - a * a - b * b))
            for c in range(b, n_3 + 1):
                t = n - a * a - b * b - c * c
                d = int(sqrt(t))
                if d < c:
                    break
                if d * d == t:
                    print(a, b, c, d)
                    exit(0)
except Exception as e:
    pass  # 如果sqrt(i)的i是负数，忽略
