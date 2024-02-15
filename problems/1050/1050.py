"""
补给
"""

from math import *


def dis(i, j):
    return sqrt((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)


def floyd():
    global w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])


n, D = map(int, input().split())
dp = [[float('inf')] * (21) for _ in range((1 << 21))]
w = [[float('inf')] * (21) for _ in range(21)]
xy = []  # 坐标
for _ in range(n): xy.append(list(map(float, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        w[i][j] = dis(i, j);
        w[j][i] = w[i][j]
        if w[i][j] > D: w[i][j] = float('inf');w[j][i] = float('inf')
floyd()
for i in range(i < (1 << n)):
    for j in range(n):    dp[i][j] = float('inf')
dp[1][0] = 0
for S in range(1 << n):
    for j in range(n):
        if (S >> j) & 1:
            for k in range(n):
                if (S ^ (1 << j)) >> k & 1:
                    dp[S][j] = min(dp[S][j], dp[S ^ (1 << j)][k] + w[k][j])
ans = inf
for i in range(1, n):   ans = min(ans, w[i][0] + dp[(1 << n) - 1][i])
print("%.2f" % ans)
