"""
最长公共子序列
"""

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(2)]
now = 0
old = 1
for i in range(1, n + 1):
    now, old = old, now
    for j in range(1, m + 1):
        dp[now][j] = max(dp[now][j - 1], dp[old][j])
        if a[i] == b[j]:
            dp[now][j] = max(dp[now][j], dp[old][j - 1] + 1)
print(dp[now][m])
