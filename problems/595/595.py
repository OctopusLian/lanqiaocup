"""
七段码
"""

N = 10
e = [[0] * N for i in range(N)]
s = [0] * N
vis = [0] * N
ans = 0


def init():
    for i in range(N):  s[i] = i


def find_set(x):  # 有路径压缩优化的查询
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def merge_set(x, y):  # 合并
    x = find_set(x)
    y = find_set(y)
    if x != y:  s[x] = s[y]


def check():
    global ans
    init()
    for i in range(1, 8):
        for j in range(1, 8):
            if e[i][j] == 1 and vis[i] == 1 and vis[j] == 1: merge_set(i, j)
    flag = 0
    for j in range(1, 8):
        if vis[j] == 1 and s[j] == j: flag += 1
    if flag == 1: ans += 1


def dfs(k):  # 深搜到第k个灯
    if k == 8:
        check()  # 检查连通性
    else:
        vis[k] = 1  # 点亮这个灯
        dfs(k + 1)  # 继续搜下一个灯
        vis[k] = 0  # 关闭这个灯
        dfs(k + 1)  # 继续搜下一个灯


e[1][2] = e[1][6] = 1
e[2][1] = e[2][3] = e[2][7] = 1
e[3][2] = e[3][4] = e[3][7] = 1
e[4][3] = e[4][5] = 1
e[5][4] = e[5][6] = e[5][7] = 1;
e[6][1] = e[6][5] = e[6][7] = 1
e[7][2] = e[7][3] = e[7][5] = e[7][6] = 1
dfs(1)  # 从第一个灯开始深搜
print(ans)
