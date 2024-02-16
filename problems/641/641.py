"""
迷宫
"""


def dfs(x, y):
    if x < 0 or y < 0 or x >= 10 or y >= 10:
        return 1
    if vis[x][y] == 1:
        return 0
    vis[x][y] = 1
    if mp[x][y] == "L":
        return dfs(x, y - 1)
    if mp[x][y] == "R":
        return dfs(x, y + 1)
    if mp[x][y] == "U":
        return dfs(x - 1, y)
    if mp[x][y] == "D":
        return dfs(x + 1, y)


mp = [['' * 10] for i in range(10)]  # 二维矩阵存迷宫
for i in range(10):
    mp[i] = list(input())  # 读迷宫
ans = 0
for i in range(10):
    for j in range(10):
        vis = [[0] * 10 for _ in range(10)]  # 初始化vis[][]
        if dfs(i, j) == 1:
            ans += 1
print(ans)
