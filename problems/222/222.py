"""
小朋友排队
"""

N = 1000010


def discretization(h):  # 数组离散化
    temp = list(set(h))
    temp.sort()
    for i in range(len(h)):
        h[i] = temp.index(h[i]) + 1


def lowbit(x):
    return x & -x


def update(x, d):
    while x <= N:
        tree[x] += d
        x += lowbit(x)


def sum_(x):
    s = 0
    while x > 0:
        s += tree[x]
        x -= lowbit(x)
    return s


n = int(input())
Hold = list(map(int, input().split()))
H = [0 for _ in range(N)]  # H是身高
for i in range(0, n):
    H[i + 1] = Hold[i] + 1
k = [0 for _ in range(N)]  # 每个小朋友的最少交换次数. 也是逆序对数量
# discretization(H)               #不需要离散化
tree = [0 for _ in range(N)]
for i in range(1, n + 1):  # 正序处理 逆序对，右边矮的
    k[i] = sum_(N - 1) - sum_(H[i])
    update(H[i], 1)
tree = [0 for _ in range(N)]
for i in range(n, 0, -1):  # 倒序处理  逆序对，左边高的
    k[i] += sum_(H[i] - 1)
    update(H[i], 1)
res = 0
for i in range(1, n + 1, 1):
    res += int((1 + k[i]) * k[i] / 2)
print(res)
