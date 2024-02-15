"""
四阶幻方
"""


def dfs(n):
    global cnt
    if n >= 4 and m[0] + m[1] + m[2] + m[3] != 34: return
    if n >= 7 and m[0] + m[4] + m[5] + m[6] != 34: return
    if n >= 10 and m[1] + m[7] + m[8] + m[9] != 34: return
    if n >= 11 and m[3] + m[6] + m[8] + m[10] != 34: return
    if n >= 12 and m[4] + m[7] + m[10] + m[11] != 34: return
    if n >= 14 and m[5] + m[8] + m[12] + m[13] != 34: return
    if n >= 15 and m[2] + m[10] + m[12] + m[14] != 34: return
    if n >= 16 and (m[6] + m[9] + m[14] + m[15] != 34
                    or m[3] + m[11] + m[13] + m[15] != 34
                    or m[0] + m[7] + m[12] + m[15] != 34): return
    if n == 16: cnt += 1
    for i in range(2, 17):  # 2~16的排列
        if vis[i] == 0:
            m[n] = i
            vis[i] = 1
            dfs(n + 1)
            vis[i] = 0


cnt = 0
m = [0] * 17
m[0] = 1  # 1被固定
vis = [0] * 17
vis[1] = 1
dfs(1)
print(cnt)
