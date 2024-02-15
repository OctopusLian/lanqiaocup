"""
合根植物
"""


def find_set(x):  # 有路径压缩优化的查询
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def merge_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return False
    s[y] = x
    return True


m, n = map(int, input().split())
k = int(input())
s = list(range(m * n + 1))  # 并查集，初始化
ans = m * n
for i in range(k):
    x, y = map(int, input().split())
    if merge_set(x, y):
        ans -= 1
print(ans)
