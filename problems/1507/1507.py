"""
编辑距离，字符串转换
"""

a = input()
a = ' ' + a  # a[0]不用，用a[1]~a[m]
b = input()
b = ' ' + b
m = len(a) - 1
n = len(b) - 1
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    dp[i][0] = i
for i in range(1, n + 1):
    dp[0][i] = i
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
print(dp[m][n])
