"""
平面切分
"""

n = int(input())
line = [tuple(map(int, input().split(" "))) for i in range(n)]
se = set(line)
line = list(se)  # 去重后的线
if line:
    ans = 2
    for i in range(1, len(line)):
        a1, b1 = line[i]
        pos = set()
        for j in range(i):
            a2, b2 = line[j]
            if a1 == a2:
                continue
            x = (b1 - b2) / (a1 - a2)
            y = a1 * x + b1
            pos.add((x, y))
        ans += len(pos) + 1
print(ans)
