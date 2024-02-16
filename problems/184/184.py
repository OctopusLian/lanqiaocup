"""
外卖店优先级
"""

n, m, T = map(int, input().split())
a = []
priorty = []
for i in range(m):
    a.append([int(i) for i in input().split()])
a = sorted(a, key=lambda a: a[0])  # 按结构体中的时间排序
order = [0 for i in range(n + 1)]
prior = [0 for i in range(n + 1)]
flag = [0 for i in range(n + 1)]
for i in range(m):
    tt = a[i][0]  # time
    idd = a[i][1]  # id
    if tt != order[idd]:
        prior[idd] -= tt - order[idd] - 1
    if prior[idd] < 0:
        prior[idd] = 0
    if prior[idd] <= 3:
        flag[idd] = 0
    prior[idd] += 2
    if prior[idd] > 5:
        flag[idd] = 1
    order[idd] = tt
for i in range(1, n + 1):
    if order[i] < T:
        prior[i] -= T - order[i]
        if prior[i] <= 3:
            flag[i] = 0
ans = 0
for i in range(n + 1):
    if flag[i] > 0:
        ans += 1
print(ans)
