"""
日志统计
"""

from bisect import bisect_left

N = int(1e5 + 50)
n, d, k = map(int, input().split())  # 读n，d，k
m = [[] for i in range(N)]
post = set()
for i in range(n):
    ts, id = map(int, input().split())  # 读ts, id
    post.add(id)
    m[id].append(ts)  # 读每个帖子的赞的时间
post = sorted(post)  # 对帖子id排序
for id in post:  # 检查每个帖子
    m[id] = sorted(m[id])  # 把某个帖子的ts排序
    for i in range(len(m[id])):  # 暴力统计这个帖子是不是热帖
        td = m[id][i] + d
        if bisect_left(m[id], td) - i >= k:
            print(id)
            break
