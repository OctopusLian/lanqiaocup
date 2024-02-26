n = 20220514
ans = 0
for i in range(1, 15000000):
    ans += i
    if ans > n and str(ans) == str(ans)[::-1]:
        break
print(ans)
