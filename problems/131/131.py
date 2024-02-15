"""
生命之树
"""

import sys

sys.setrecursionlimit(50020)  # 设置递归深度


def dfs(u, fa):
    global res
    for son in tree[u]:
        if son != fa:
            dfs(son, u)
            if dp[son] > 0:
                dp[u] += dp[son]
    res = max(res, dp[u])


n = int(input())
tree = [list() for i in range(n + 1)]

w = [0 for i in range(n + 1)]
dp = [0 for i in range(n + 1)]
res = 0

w[1:n] = map(int, input().split())
dp = w
for i in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dfs(1, -1)
print(res)
