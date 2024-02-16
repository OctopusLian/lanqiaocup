"""
逆序对
"""

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
for i in range(n):  a[a.index(b[i])] = i + 1
tree = [0] * (n + 1)


def lowbit(x):
    return x & -x


def update(x, d):
    while x < n:
        tree[x] += d
        x += lowbit(x)


def sum(x):
    ans = 0
    while x > 0:
        ans += tree[x]
        x -= lowbit(x)
    return ans


res = 0
a.insert(0, 0)  # 在最前面加个0
for i in range(len(a) - 1, 0, -1):
    update(a[i], 1)
    res += sum(a[i] - 1)

print(res)
