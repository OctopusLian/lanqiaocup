"""
砝码称重
"""

n = int(input())
w = list(map(int, input().split()))
ans = set()
ans.add(w[0])
for i in w[1:]:
    for j in ans.copy():
        ans.add(i)
        ans.add(j + i)
        if j - i != 0:
            ans.add(abs(j - i))
print(len(ans))
