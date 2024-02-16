"""
错误票据
"""

n = int(input())
a = []
for i in range(n):
    num = input().split()
    for j in range(len(num)):
        a.append(int(num[j]))  # 读取n行数据，存到a[]
a.sort()
for i in range(a[0], a[0] + len(a)):
    if i not in a:     ans1 = i
    if a.count(i) == 2:  ans2 = i
print(ans1, ans2)
