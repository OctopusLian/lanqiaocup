"""
剪格子
"""


def dfs(x, y, c, s):
    global sum_num, ans
    if 2 * s > sum_num: return
    if 2 * s == sum_num:
        if ans > c and vis[0][0] == 1: ans = c
        return
    vis[x][y] = 1
    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for u, v in dir:
        tx, ty = x + u, y + v
        if 0 <= tx <= n - 1 and 0 <= ty <= m - 1:
            if vis[tx][ty] == 0:
                dfs(tx, ty, c + 1, s + a[x][y])
    vis[x][y] = 0


m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
sum_num = 0
for i in a:  sum_num += sum(i)
if sum_num / 2 != sum_num // 2:
    print(0)
    exit()  # 无解
ans = 100000
dfs(0, 0, 0, 0)
print(ans)
