"""
https://www.lanqiao.cn/problems/2117/learning/?page=1&first_category_id=1&problem_id=2117
砍竹子
"""

from math import *

f = [[0] * 10 for _ in range(200010)]  # 二维数组初始化
stk = [0] * 10  # 一维数组初始化
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = a[i]
    top = 0
    while x > 1:
        top += 1
        stk[top] = x
        x = floor(sqrt(floor(x / 2) + 1))
    ans += top
    k = top
    j = 0
    while k > 0:
        f[i][j] = stk[k]
        k -= 1
        j += 1
for j in range(10):
    for i in range(1, n):
        if f[i][j] > 0 and f[i][j] == f[i - 1][j]:
            ans -= 1
print(ans)
