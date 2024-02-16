"""
灵能传输
"""

T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] + a
    for i in range(1, n + 1):
        s[i] += s[i - 1]  # 前缀和
    s0 = 0
    sn = s[n]
    if s0 > sn:  sn, s0 = s0, sn  # 交换: swap(s0, sn)
    s.sort()
    for i in range(n + 1):  # 找s[0]和s[n]的位置
        if s[i] == s0:
            s0 = i
            break
    for i in range(n, -1, -1):
        if s[i] == sn:
            sn = i
            break
    L, R = 0, n
    a = [0 for i in range(n + 1)]
    a[n] = s[n]
    vis = [True for i in range(n + 1)]
    for i in range(s0, -1, -2):
        a[L] = s[i]
        L += 1
        vis[i] = False
    for i in range(sn, n + 1, 2):
        a[R] = s[i]
        R -= 1
        vis[i] = False
    for i in range(n + 1):
        if vis[i]: a[L] = s[i]; L += 1
    res = 0
    for i in range(n): res = max(res, abs(a[i + 1] - a[i]))
    print(res)
