"""
双向排序
"""

stk = []  # 空栈
n, m = map(int, input().split())
for i in range(m):
    p, q = map(int, input().split())
    if p == 0:  # 0操作
        while stk and stk[len(stk) - 1][0] == 0:
            q = max(q, stk.pop()[1])
        while len(stk) >= 2 and stk[len(stk) - 2][1] <= q:
            stk.pop()
            stk.pop()
        stk.append([0, q])
    elif stk:
        while stk and stk[len(stk) - 1][0] == 1:
            q = min(q, stk.pop()[1])
        while len(stk) >= 2 and stk[len(stk) - 2][1] >= q:
            stk.pop()
            stk.pop()
        stk.append([1, q])
k, L, R = n, 1, n
ans = [0] * (n + 1)
for x, y in stk:  # 逐个处理栈元素
    if x == 0:
        while R > y and L <= R:
            ans[R] = k
            k = k - 1
            R = R - 1
    else:
        while L < y and L <= R:
            ans[L] = k
            k = k - 1
            L = L + 1
    if L > R:
        break
if x == 0:
    while L <= R:
        ans[L] = k
        k = k - 1
        L = L + 1
else:
    while L <= R:
        ans[R] = k
        k = k - 1
        R = R - 1
for i in range(1, n + 1):
    print(ans[i], end=' ')
