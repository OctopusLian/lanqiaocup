"""
区间最大值
"""

from math import *

N = 100001
dp = [[0 for col in range(40)] for row in range(N)]  # 定义一个二维数组


def st_init():
    global dp
    for i in range(1, n + 1): dp[i][0] = a[i]
    p = int(log2(n))
    for k in range(1, p + 1):
        for s in range(1, n + 2 - (1 << k)):
            dp[s][k] = max(dp[s][k - 1], dp[s + (1 << (k - 1))][k - 1])


def st_query(L, R):
    k = int(log2(R - L + 1))
    return max(dp[L][k], dp[R - (1 << k) + 1][k])


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)  # 从a[1]开始，不用a[0]
st_init()
for i in range(1, m + 1):
    L, R = map(int, input().split())
    print(st_query(L, R))
