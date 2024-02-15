"""
出差
"""

n, m = map(int, input().split())
t = [0] + [int(i) for i in input().split()]  # 不用t[0]，从t[1]开始
e = []  # 简单的数组存图
for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    e.append([a, b, c])
    e.append([b, a, c])  # 双向边
dist = [0x3f3f3f3f] * (n + 1)
dist[1] = 0
for k in range(1, n + 1):
    for a, b, c in e:
        res = t[b]
        if b == n: res = 0
        dist[b] = min(dist[b], dist[a] + c + res)
print(dist[n])
