"""
过河卒
"""

dp = [[0] * 25 for i in range(25)]
s = [[0] * 25 for i in range(25)]
bx, by, mx, my = [int(i) for i in input().split()]
bx += 2
by += 2
mx += 2
my += 2
dp[2][1] = 1
s[mx][my] = 1
s[mx - 2][my - 1] = 1
s[mx - 2][my + 1] = 1
s[mx + 2][my - 1] = 1
s[mx + 2][my + 1] = 1
s[mx - 1][my + 2] = 1
s[mx - 1][my - 2] = 1
s[mx + 1][my + 2] = 1
s[mx + 1][my - 2] = 1
for i in range(2, bx + 1):
    for j in range(2, by + 1):
        if s[i][j] == 1:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[bx][by])
