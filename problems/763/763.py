"""
装箱问题
"""

dp = [0] * 20010
w = [0] * 40
V = int(input())
n = int(input())
for i in range(1, n + 1):   w[i] = int(input())
for i in range(1, n + 1):
    for j in range(V, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + w[i])
print(V - dp[V])
