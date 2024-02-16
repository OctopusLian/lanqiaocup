"""
统计子矩阵
"""

n, m, k = map(int, input().split())
a = [[0] for i in range(n)]
a.insert(0, [0] * (m + 1))
for i in range(1, n + 1):  # 从a[1][1]开始，读矩阵
    a[i].extend(map(int, input().split()))
s = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + a[i][j]
ans = 0
for i1 in range(1, n + 1):
    for i2 in range(i1, n + 1):
        j1 = 1
        z = 0
        for j2 in range(1, m + 1):
            z += s[i2][j2] - s[i1 - 1][j2]
            while z > k:
                z -= s[i2][j1] - s[i1 - 1][j1]
                j1 += 1
            ans += j2 - j1 + 1
print(ans)
