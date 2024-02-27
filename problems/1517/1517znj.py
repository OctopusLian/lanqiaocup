import os
import sys

# 请在此输入您的代码
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 代替方向:下、右、上、左
m, n = map(int, input().split(" "))
metrix = [0] * m
for i in range(m):
    metrix[i] = list(map(int, input().split(' ')))
d = 0
# 用于方向的变换，相当于游标
count = 0
# 记录访问数字的个数，不能超过m*n
x, y = -1, 0
# 记录初始位置
while count < m * n:
    x1, y1 = x + dir[d][0], y + dir[d][1]
    # 先对位置进行变换，再判断位置的是否合理
    if x1 >= m or x1 < 0 or y1 >= n or y1 < 0 or metrix[x1][y1] == -1:
        # 位置不正确的情况，需要换方向了
        d = (d + 1) % 4
        x, y = x + dir[d][0], y + dir[d][1]
    else:
        # 位置合理的情况
        x, y = x1, y1
    print(metrix[x][y], end=' ')
    count += 1
    metrix[x][y] = -1
