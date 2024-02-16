"""
矩阵计数
"""

N, M = list(map(int, input().split()))
state = 2 ** M
row = []
for i in range(state):
    num, flag = 0, False
    temp = i
    while temp:
        if temp & 1:
            num += 1
        else:
            num = 0
        if num == 3:
            flag = True
            break
        temp >>= 1
    if not flag:
        row.append(i)

dp = [[[0 for _ in range(state)] for __ in range(state)] for ___ in range(N)]
for i in row:
    dp[0][i][0] = 1
for i in range(1, N):
    for j in row:
        for k in row:
            for p in row:
                if j & k & p == 0:  dp[i][j][k] += dp[i - 1][k][p]
ans = 0
for i in row:
    ans += sum(dp[N - 1][i])
print(ans)
