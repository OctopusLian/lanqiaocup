"""
最长不下降子序列
"""


class node:
    def __init__(self, l, r, v):
        self.l = l
        self.r = r
        self.v = v


def pushup(u):
    tree[u].v = max(tree[u << 1].v, tree[u << 1 | 1].v)


def build(p, pl, pr):
    if pl == pr:
        tree[p] = node(pl, pr, 0)
    else:
        tree[p] = node(pl, pr, 0)
        mid = pl + pr >> 1
        build(p << 1, pl, mid)
        build(p << 1 | 1, mid + 1, pr)


def update(p, x, v):
    if tree[p].l == tree[p].r:
        tree[p].v = v
    else:
        mid = tree[p].l + tree[p].r >> 1
        if x <= mid:
            update(p << 1, x, v)
        else:
            update(p << 1 | 1, x, v)
        pushup(p)


def query(p, pl, pr):
    if pl <= tree[p].l and pr >= tree[p].r:  return tree[p].v
    mid = tree[p].l + tree[p].r >> 1
    res = 0
    if pl <= mid:    res = max(res, query(p << 1, pl, pr))
    if pr > mid:     res = max(res, query(p << 1 | 1, pl, pr))
    return res


def find(x):  # x是第几大的数。用于离散化，把数x离散化为第几大
    L, R = 0, n - 1
    while L < R:
        mid = (L + R + 1) >> 1
        if num[mid] <= x:
            L = mid
        else:
            R = mid - 1
    return L


n, k = list(map(int, input().split()))
b = [0] + list(map(int, input().split()))  # 加一个b[0]，从b[1]开始到b[n]
n = n + 1
num = sorted(b)  # 排序后返回，复制给num
a = [0] * n
for i in range(0, n): a[i] = find(b[i])  # 把b离散化为a
tree = [None] * (4 * n)
build(1, 1, n)
dp = [0] * (n + 10)
for i in range(1, n):
    dp[i] = query(1, 0, a[i]) + 1
    update(1, a[i], dp[i])
build(1, 1, n)
ans = 0
for i in range(n - 1, k, -1):  # 从后往前，每次暴力修改k个
    ans = max(ans, dp[i - k] + k - 1 + query(1, a[i - k], n) + 1)
    tmp = query(1, a[i], n) + 1
    ans = max(ans, tmp + k)
    update(1, a[i], tmp)
print(ans)
