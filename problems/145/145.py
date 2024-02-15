"""
数位递增的数
"""

n = int(input())
ans = 0
for i in range(1, n):
    s = list(str(i))
    if s == sorted(s):  # 注意不能用sort()
        ans += 1
print(ans)
