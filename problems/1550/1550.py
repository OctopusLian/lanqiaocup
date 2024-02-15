"""
矩阵相乘
"""

n, m, k = map(int, input().split())
A = []
B = []
C = [[0] * k for i in range(n)]

for i in range(n):   A.append(list(map(int, input().split())))
for i in range(m):   B.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        for l in range(k):
            C[i][l] += A[i][j] * B[j][l]
for i in range(n):
    for j in range(k):
        print(C[i][j], end=" ")
    print()  # 换行
