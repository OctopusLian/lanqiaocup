"""
数的拆分
"""

from math import *

N = 4000

prime = [0] * N
vis = [0] * N
cnt = 0


def E_sieve():
    global cnt
    for i in range(2, N):
        if not vis[i]:
            cnt += 1
            prime[cnt] = i
        for j in range(i * i, N, i):
            vis[j] = 1


def solve():
    a = int(input())
    for i in range(1, cnt + 1):
        c = 0
        while a % prime[i] == 0:
            a /= prime[i]
            c += 1
        if c == 1:
            print("no")
            return

    k = int(sqrt(a))
    if k * k == a:
        print("yes")
        return  # 检查n是否为平方数
    k = int(pow(a, 1 / 3))
    if k * k * k == a:
        print("yes")
        return  # 检查n是否为立方数
    print("no")


E_sieve()
T = int(input())
for i in range(T): solve()