"""
坐标搜寻
"""

from math import *


def dist(i, j):
    return sqrt((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)


n = int(input())
dp = [[float('inf')] * (21) for _ in range((1 << 16))]
xy = [list([float(0), float(0)])]  # 坐标
for _ in range(n): xy.append(list(map(float, input().split())))
n = n + 1
dp[1][0] = 0
for S in range(1, 1 << n):
    for j in range(n):
        for k in range(n):
            if (((S >> j) & 1) and ((S ^ (1 << j)) >> k & 1)):
                dp[S][j] = min(dp[S][j], dp[S ^ (1 << j)][k] + dist(k, j))
ans = dp[(1 << n) - 1][0]
for i in range(1, n):
    p = dp[(1 << n) - 1][i]
    if ans > p:
        ans = p
print("%.2f" % ans)
