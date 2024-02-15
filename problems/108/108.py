"""
发现环
"""


def find_set(x):  # 有路径压缩优化的查询
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def merge_set(x, y):
    global start
    tmp = x
    x = find_set(x)
    y = find_set(y)
    if x != y:
        s[y] = s[x]  # 合并
    else:
        start = tmp


def dfs(x, step):  # 从起点start出发找一条回到start的环路
    global flag, start, vis, tot, ring
    if flag == 1: return
    if x == start:
        if vis[x] == 1:
            tot = step - 1
            flag = 1
            return
    ring[step] = x
    for y in edge[x]:
        if vis[y] == 0:
            vis[y] = 1
            dfs(y, step + 1)
            vis[y] = 0


N = 100010
start = 0
tot = 0
vis = [0] * N
ring = [0] * N
s = list(range(N))  # 并查集，定义、初始化 s=[0,1,2,3,……]
n = int(input())
edge = [[] for i in range(n + 1)]  # 邻接表
for i in range(n):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
    merge_set(u, v)
flag = 0
dfs(start, 1)
ans = ring[1:1 + tot]  # 拷贝出来
ans.sort()  # 排序
for i in range(tot): print(ans[i], end=' ')
