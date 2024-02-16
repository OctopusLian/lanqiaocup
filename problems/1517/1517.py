"""
https://www.lanqiao.cn/problems/1517/learning/?page=1&first_category_id=1&problem_id=1517
回形取数
"""

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 4个方向
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(input().split())
x, y = -1, 0
d = 0
sum = 0
while sum < m * n:
    sum = sum + 1
    nx, ny = x + dir[d][0], y + dir[d][1]
    if nx < 0 or nx >= m or ny < 0 or ny >= n or a[nx][ny] == -1:
        d = (d + 1) % 4
        x, y = x + dir[d][0], y + dir[d][1]
    else:
        x, y = nx, ny
    print(a[x][y], end=' ')
    a[x][y] = -1  # 标记这个坐标点已经取过
