"""
修建公路1
"""

e = []
s = []  # 并查集


def find(x):  # 查询并查集，返回x的根
    if s[x] == x:  return x
    s[x] = find(s[x])  # 路径压缩
    return s[x]


def kruskal():
    ans = 0
    e.sort(key=lambda tup: tup[2])  # 对边做排序
    for i in range(n + 1):  s.append(i)  # 并查集初始化
    for i in range(m):
        x, y = e[i][0], e[i][1]
        e1, e2 = find(x), find(y)
        if e1 == e2:
            continue  # 属于同一个集：产生了圈，丢弃
        else:
            ans += e[i][2]
            s[s[x]] = s[y]  # 合并
    find(1)
    for i in range(2, n + 1):
        if find(i) != s[i - 1]:
            print("-1"); return
    print(ans)
    return


n, m = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    e.append((u, v, w))  # 读边
kruskal()
