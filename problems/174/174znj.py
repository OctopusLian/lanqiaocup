n, s = map(int, input().split())
a = list(map(int, input().split()))
res = 0
a.sort()

avg = s / n
for i in range(n):
    newavg = s / (n - i)
    if (a[i] < newavg):
        s -= a[i]
        res += (a[i] - avg) ** 2
    else:
        res += ((newavg - avg) ** 2) * (n - i)  # 平分方差
        break
res = (res / n) ** 0.5
print("{:.4f}".format(res))
