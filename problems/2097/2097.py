"""
青蛙过河
"""


def check(mid):
    for i in range(mid, n):
        if sum[i] - sum[i - mid] < 2 * x:
            return False
    return True


n, x = map(int, input().split())
h = list(map(int, input().split()))
sum = [0, h[0]]
for i in range(1, len(h)):
    sum.append(h[i] + sum[i])
L = 0
R = 100000
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        R = mid - 1
    else:
        L = mid + 1
print(L)