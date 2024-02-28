n = int(input())
S = 0
a = list(map(int, input().split()))
s1 = sum(a)
for i in range(0, n):
    s1 -= a[i]
    S += a[i] * s1
print(S)
