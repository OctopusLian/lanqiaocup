"""
荷马史诗
"""

from heapq import *

n, k = map(int, input().split())
w = []
for i in range(n):   w.append(int(input()))
pq = [(i, 0) for i in w]
while (n - 1) % (k - 1) != 0:
    pq += [(0, 0)]
    n += 1
heapify(pq)  # 让列表具备堆特征
ans, x = 0, 0
while len(pq) > 1:
    s = 0
    for i in range(k):
        tmp = heappop(pq)
        s += tmp[0]
        x = max(x, tmp[1])
    ans += s
    heappush(pq, (s, x + 1))
print(ans)
print(x + 1)
