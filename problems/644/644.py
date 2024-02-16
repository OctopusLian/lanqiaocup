"""
方格分割
"""

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右4个方向
vis = [[1] * 7 for i in range(7)]
cnt = 0


def dfs(x, y):
    global cnt
    if x == 0 or y == 0 or x == 6 or y == 6:
        cnt += 1
        return
    # 当前点和对称点都标注访问
    vis[x][y], vis[6 - x][6 - y] = 0, 0
    for i in range(0, 4):
        newx = x + dir[i][0]  # 新坐标
        newy = y + dir[i][1]
        if newx < 0 or newx > 6 or newy < 0 or newy > 6:
            continue
        if vis[newx][newy]:
            dfs(newx, newy)
    vis[x][y], vis[6 - x][6 - y] = 1, 1


dfs(3, 3)
print(cnt // 4)