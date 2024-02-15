"""
分巧克力
"""


def check(d):
    global w, h
    res = 0
    for i in range(len(w)):
        res += (w[i] // d) * (h[i] // d)
    if res >= k:
        return True
    return False


n, k = map(int, input().split())
w = []
h = []
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    h.append(b)
L, R = 1, 10000
while L < R:
    mid = (L + R) // 2
    if check(mid):
        L = mid + 1
    else:
        R = mid
print(L - 1)
