"""
暴力法

能过40%样例
"""

n = int(input())
a = [int(i) for i in input().split()]
s = 0
for i in range(n):
    for j in range(i+1,n):
        s += a[i] * a[j]
print(s)