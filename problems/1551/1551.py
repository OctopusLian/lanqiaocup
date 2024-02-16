"""
方阵幂次
"""


def multi(A, B):
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    if n1 != m2:
        return None
    C = [[0] * n2 for i in range(m1)]
    for i in range(m1):
        for k in range(n1):
            for j in range(n2):
                C[i][j] += A[i][k] * B[k][j]
    return C


def power(A, n):
    N = len(A)
    res = [[0] * N for i in range(N)]
    for i in range(N): res[i][i] = 1
    while n:
        if n % 2:  res = multi(res, A)
        A = multi(A, A)
        n //= 2
    return res


s, q = map(int, input().split())
A = []
for i in range(s):
    A.append(list(map(int, input().split())))
res = power(A, q)
for row in res:
    for c in row: print(c, end=' ')
    print()
