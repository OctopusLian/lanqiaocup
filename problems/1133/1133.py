"""
区间修改，区间求和
"""


def build(p, pl, pr):  # 建树
    if pl == pr:
        tree[p] = a[pl]
        return
    mid = (pl + pr) >> 1
    build(p << 1, pl, mid)
    build(p << 1 | 1, mid + 1, pr)
    tree[p] = tree[p << 1] + tree[p << 1 | 1]  # push_up(p)


def addtag(p, pl, pr, d):  # 给结点p打tag标记，并更新tree
    tag[p] += d  # 打上tag标记
    tree[p] += d * (pr - pl + 1);  # 计算新的tree


def push_down(p, pl, pr):
    if tag[p] > 0:  # 有tag标记，这是以前做区间修改时留下的
        mid = (pl + pr) >> 1
        addtag(p << 1, pl, mid, tag[p])  # 把tag标记传给左子树
        addtag(p << 1 | 1, mid + 1, pr, tag[p])  # 把tag标记传给右子树
        tag[p] = 0  # p自己的tag被传走了，归0


def update(L, R, p, pl, pr, d):
    if L <= pl and R >= pr:
        addtag(p, pl, pr, d)
        return
    push_down(p, pl, pr)  # 将懒惰标记传递给孩子
    mid = (pl + pr) >> 1
    if L <= mid:     update(L, R, p << 1, pl, mid, d)
    if R >= mid + 1: update(L, R, p << 1 | 1, mid + 1, pr, d)
    tree[p] = tree[p << 1] + tree[p << 1 | 1]  # push_up(p)


def query(L, R, p, pl, pr):
    if L <= pl and R >= pr:   return tree[p]
    push_down(p, pl, pr)
    res = 0
    mid = (pl + pr) >> 1
    if L <= mid:  res += query(L, R, p << 1, pl, mid, )
    if R > mid:  res += query(L, R, p << 1 | 1, mid + 1, pr)
    return res


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
tag = [0] * (len(a) << 2)
tree = [0] * (len(a) << 2)
build(1, 1, n)  # 建树
for i in range(m):
    w = list(map(int, input().split()))
    if len(w) == 3:  # 区间询问：[L,R]的区间和
        q, L, R = w
        print(query(L, R, 1, 1, n))
    else:  # 区间修改：把[L,R]的每个元素加上d
        q, L, R, d = w
        update(L, R, 1, 1, n, d)