"""
选数异或
"""

N = 100010
Left = [0] * N
pos = [0] * ((1 << 20) + 10)
tree = [0] * (N << 2)  # 4倍


def build(p, pl, pr):
    if pl == pr:
        tree[p] = Left[pl]
        return
    mid = (pl + pr) >> 1
    build(p << 1, pl, mid)  # p<<1 是左儿子
    build(p << 1 | 1, mid + 1, pr)  # p<<1|1是右儿子
    tree[p] = max(tree[p << 1], tree[p << 1 | 1])  # push_up


def query(p, pl, pr, L, R):
    if L <= pl and pr <= R:  return tree[p]
    mid = (pl + pr) >> 1
    res = 0
    if L <= mid:  res = max(res, query(p << 1, pl, mid, L, R))
    if R > mid:   res = max(res, query(p << 1 | 1, mid + 1, pr, L, R))
    return res


n, m, x = map(int, input().split())
a = list(input().split())
a.insert(0, 0)  # 加个a[0]。从a[1]开始
for i in range(1, n + 1):
    a[i] = int(a[i])
    Left[i] = pos[a[i] ^ x]
    pos[a[i]] = i
build(1, 1, n)
for i in range(m):
    L, R = map(int, input().split())
    if query(1, 1, n, L, R) >= L:
        print('yes')
    else:
        print('no')
