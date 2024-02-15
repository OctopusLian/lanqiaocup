"""
防御力
"""


def cmp(x):
    return x[1]


n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n1): a[i] = (i + 1, a[i])
for i in range(n2): b[i] = (i + 1, b[i])
a.sort(key=cmp)
b.sort(key=cmp, reverse=True)
s = input()
idx1, idx2 = 0, 0
for i in range(n1 + n2):
    if s[i] == '1':
        print("B%d" % b[idx1][0]);
        idx1 += 1
    else:
        print("A%d" % a[idx2][0]);
        idx2 += 1
print("E")
