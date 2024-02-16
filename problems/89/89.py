"""
路径之谜
"""


def dfs(x, y):
    if a[x] < 0 or b[y] < 0: return
    if x == n - 1 and y == n - 1:
        ok = 1
        for i in range(n):
            if a[i] != 0 or b[i] != 0: ok = 0; break
        if ok == 1:
            for i in range(len(path)): print(path[i], end=' ')
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tx = x + d[0];
        ty = y + d[1]
        if n > tx >= 0 == vis[tx][ty] and 0 <= ty < n:
            vis[tx][ty] = 1
            path.append(tx * n + ty)  # 进栈，记录路径
            a[tx] -= 1
            b[ty] -= 1
            dfs(tx, ty)
            path.pop()  # 出栈，DFS回溯
            a[tx] += 1
            b[ty] += 1
            vis[tx][ty] = 0


n = int(input())
vis = [[0] * n for i in range(n)]
path = [0]  # 用栈记录路径
b = list(map(int, input().split()))
a = list(map(int, input().split()))
vis[0][0] = 1
a[0] -= 1
b[0] -= 1
dfs(0, 0)
