"""
大臣的旅费
"""


def dfs(u):
    global maxlen
    vis[u] = 1
    for v, edge in e[u]:
        if vis[v] == 1:
            continue
        dfs(v)
        maxlen = max(maxlen, dp[u] + dp[v] + edge)
        dp[u] = max(dp[u], dp[v] + edge)


n = int(input())
e = [list() for i in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    e[a].append((b, c))
    e[b].append((a, c))
maxlen = 0
vis = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]
dfs(1)
print(maxlen * 10 + maxlen * (maxlen + 1) // 2)
