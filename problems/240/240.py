"""
排列数
"""

N = 520
dp = [[0] * N for i in range(N)]
n, k = map(int, input().split())
dp[1][1] = 1
dp[2][1] = 2
for i in range(3, n + 1):
    ki = min(k, i)
    for j in range(1, ki + 1):
        dp[i][j] += dp[i - 1][j] * j + dp[i - 1][j - 1] * 2
        if j > 1:
            dp[i][j] += dp[i - 1][j - 2] * (i - j)
print(dp[n][k] % 123456)
