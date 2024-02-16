"""
蓝桥幼儿园
"""

N = 800_005
s = []  # 并查集


def init_set():  # 初始化
    for i in range(N):
        s.append(i)


def find_set(x):  # 有路径压缩优化的查询
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def merge_set(x, y):  # 合并
    x = find_set(x)
    y = find_set(y)
    if x != y:
        s[x] = s[y]


n, m = map(int, input().split())
init_set()
for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:   merge_set(x, y);
    if op == 2:
        if find_set(x) == find_set(y):
            print("YES")
        else:
            print("NO")
