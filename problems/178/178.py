"""
全球变暖
"""

from collections import *


def bfs(x, y):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((x, y))
    vis[x][y] = 1
    global flag
    while q:
        t = q.popleft()
        tx, ty = t[0], t[1]
        if mp[tx][ty + 1] == '#' and mp[tx][ty - 1] == '#' and \
                mp[tx + 1][ty] == '#' and mp[tx - 1][ty] == '#':
            flag = 1
        for i in range(4):
            nx = tx + d[i][0]
            ny = ty + d[i][1]
            if vis[nx][ny] == 0 and mp[nx][ny] == "#":
                q.append((nx, ny))
                vis[nx][ny] = 1


n = int(input())
mp = []
for i in range(n):
    mp.append(list(input()))
vis = []
for i in range(n):
    vis.append([0] * n)
ans = 0
for i in range(n):
    for j in range(n):
        if vis[i][j] == 0 and mp[i][j] == "#":
            flag = 0
            bfs(i, j)
            if flag == 0:
                ans += 1
print(ans)
