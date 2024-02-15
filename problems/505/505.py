"""
数字三角形
"""

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
# 数组a[][]同时当成dp[][]用
for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            a[i][j] += a[i - 1][j]  # 最左边元素
        elif j == i:
            a[i][j] += a[i - 1][j - 1]  # 最右边元素
        else:
            a[i][j] += max(a[i - 1][j - 1:j + 1])
if n & 1:  # 如果是奇数行，则返回最中间值
    print(a[-1][n // 2])
else:  # 偶数行则返回中间较大值
    print(max(a[-1][n // 2 - 1], a[-1][n // 2]))
