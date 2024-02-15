"""
蓝桥骑士
"""

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
d = []
for i in a:
    if not d or i > d[-1]:
        d.append(i)
    else:
        x = bisect_left(d, i)
        d[x] = i
print(len(d))
