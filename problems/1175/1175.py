"""
小明的背包2
"""

n, C = map(int, input().split())
dp = [0] * (C + 1)
for i in range(n):
    ci, wi = map(int, input().split())
    for j in range(ci, C + 1):
        dp[j] += dp[j - ci] + wi
print(dp[-1])
