"""
跳石头
"""

len, n, m = map(int, input().split())
stone = []  # 石头i和到起起点的距离


def check(d):
    num = 0
    pos = 0
    for i in range(0, n):  # 0到n-1作为石头下标
        if stone[i] - pos < d:  # 第i块可以搬走
            num += 1
        else:
            pos = stone[i]
    if num <= m:
        return True
    else:
        return False


for i in range(n):
    t = int(input())
    stone.append(t)
L, R = 0, len
while L < R:
    mid = L + (R - L) // 2
    if check(mid):
        L = mid + 1
    else:
        R = mid - 1
if check(L):
    print(L)
else:
    print(L - 1)
