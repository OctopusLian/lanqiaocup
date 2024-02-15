"""
最大数
"""

N = 100001
INF = 0X7FFFFFFF
tree = [0] * (N << 2)  # 4倍


def build(p, pl, pr):
    if pl == pr:
        tree[p] = -INF
        return
    mid = (pl + pr) >> 1
    build(p << 1, pl, mid)  # p<<1 是左儿子
    build(p << 1 | 1, mid + 1, pr)  # p<<1|1是右儿子
    tree[p] = max(tree[p << 1], tree[p << 1 | 1])  # push_up


def update(p, pl, pr, L, R, d):
    if L <= pl and pr <= R:
        tree[p] = d
        return
    mid = (pr + pl) >> 1
    if L <= mid:
        update(p << 1, pl, mid, L, R, d)
    if R > mid:
        update(p << 1 | 1, mid + 1, pr, L, R, d)
    tree[p] = max(tree[p << 1], tree[p << 1 | 1])
    return


def query(p, pl, pr, L, R):
    res = -INF
    if L <= pl and pr <= R:
        return tree[p]
    mid = (pl + pr) >> 1
    if L <= mid:
        res = max(res, query(p << 1, pl, mid, L, R))
    if R > mid:
        res = max(res, query(p << 1 | 1, mid + 1, pr, L, R))
    return res


m, D = map(int, input().split())
build(1, 1, N)  # 不用build()，这样写也行：update(1,1,N,1,N,-INF);
cnt = 0
t = 0
for i in range(m):
    op = list(input().split())
    if op[0] == 'A':
        cnt += 1
        update(1, 1, N, cnt, cnt, (int(op[1]) + t) % D)
    if op[0] == 'Q':
        t = query(1, 1, N, cnt - int(op[1]) + 1, cnt)
        print(t)
