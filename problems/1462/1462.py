"""
回路计数
"""

from math import gcd
n = 21
m = 1 << n
dp = [[0 for j in range(n)] for i in range(m)]
dist = [[False for j in range(n)] for i in range(n)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if gcd(i, j) == 1:
            dist[i - 1][j - 1] = True
dp[1][0] = 1
for S in range(1, m):
    for j in range(n):
        if S >> j & 1:
            for k in range(n):
                if S - (1 << j) >> k & 1 and dist[k][j]:
                    dp[S][j] += dp[S - (1 << j)][k]
print(sum(dp[m - 1]) - dp[m - 1][0])