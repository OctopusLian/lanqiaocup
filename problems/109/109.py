"""
分考场
"""


def dfs(x, room):
    global num, p
    if room > num: return
    if x > n:
        if room < num: num = room
        return
    for j in range(1, room + 1):
        k = 0
        while p[j][k] and a[x][p[j][k]] == 0:  k += 1
        if p[j][k] == 0:
            p[j][k] = x
            dfs(x + 1, room)
            p[j][k] = 0
    p[room + 1][0] = x
    dfs(x + 1, room + 1)
    p[room + 1][0] = 0


n = int(input())
m = int(input())
num = 110
p = [[0 for i in range(n + 1)] for j in range(n + 1)]
a = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    a[u][v] = a[v][u] = 1
dfs(1, 0)
print(num)
