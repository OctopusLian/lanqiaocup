n = int(input())
for i in range(1, n + 1):
    print(max(i - 1, n - i) * 2)
