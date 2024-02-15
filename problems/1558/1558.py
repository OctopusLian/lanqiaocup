"""
找素数
"""

from math import *

N = 1000005
vis = [True] * N  # 标记[2,sqrt(b)]是否为素数
prime = [0] * N  # 存[a,b]的素数
seg_prime = [True] * (N)  # 标记[a,b]是否为素数


def seg_sieve(a, b):
    for i in range(2, int(sqrt(b)) + 1):
        if vis[i]:  # 是素数
            for j in range(i * i, int(sqrt(b)), i):
                vis[j] = False
            for j in range(max(2, (a + i - 1) // i) * i, b + 1, i):
                seg_prime[j - a] = False
    num = 0
    for i in range(0, b - a + 1):
        if seg_prime[i]:
            prime[num] = i + a
            num += 1
    print(num)


a, b = map(int, input().split())
seg_sieve(a, b)
