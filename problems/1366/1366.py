"""
随机数据下的最短路径问题
"""

import heapq


def spfa(s):
    dis[s] = 0
    hp = []
    heapq.heappush(hp, s)
    inq = [0] * (n + 1)
    inq[s] = 1
    while hp:
        u = heapq.heappop(hp)
        inq[u] = 0
        if dis[u] == INF: continue
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                if inq[v] == 0:
                    heapq.heappush(hp, v)
                    inq[v] = 1


n, m, s = map(int, input().split())
e = [[] for i in range(n + 1)]
INF = 1 << 64
dis = [INF] * (n + 1)
for i in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))
spfa(s)
for i in range(1, n + 1):
    if dis[i] >= INF:
        print("-1", end=' ')
    else:
        print(dis[i], end=' ')
