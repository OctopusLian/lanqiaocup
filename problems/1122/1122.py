"""
蓝桥王国
"""
import array
import heapq


def dij(s):
    vis = [0 for i in range(n + 1)]
    hp = []
    dis[s] = 0
    heapq.heappush(hp, (0, s))
    while hp:
        u = heapq.heappop(hp)[1]
        if vis[u]:
            continue
        vis[u] = 1
        for i in range(len(G[u])):
            v, w = G[u][i], W[u][i]
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(hp, (dis[v], v))


n, m = map(int, input().split())
s = 1
G = [array.array('i') for i in range(n + 1)]
W = [array.array('i') for i in range(n + 1)]
INF = 1 << 64
dis = [INF] * (n + 1)
for i in range(m):
    u, v, w = map(int, input().split())
    G[u].append(v)
    W[u].append(w)
dij(s)
for i in range(1, n + 1):
    if dis[i] >= INF:
        print("-1", end=' ')
    else:
        print(dis[i], end=' ')