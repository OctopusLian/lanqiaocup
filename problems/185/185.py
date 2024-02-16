"""
修改数组
"""


def find_set(x):  # 有路径压缩优化的查询
    if x != s[x]:
        s[x] = find_set(s[x])  # 集的根是最新的一个数
    return s[x]


N = 1000002
s = list(range(N))  # 并查集，定义、初始化 s=[0,1,2,3,……]
n = int(input())
A = [int(i) for i in input().split()]
for i in range(n):
    root = find_set(A[i])
    A[i] = root
    s[root] = find_set(root + 1)  # 加1
for i in A:
    print(i, end=' ')
