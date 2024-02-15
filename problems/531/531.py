"""
奖学金
"""

count = int(input())
info = []
for i in range(count):
    info.append([i + 1] + list(map(int, input().split())))
for i in info:
    i.append(sum(i) - info.index(i) - 1)
index = reversed((4, 1, 0))
for i in index:
    info.sort(key=lambda x: x[i], reverse=True)
for i in range(0, 5):
    print(info[i][0], info[i][4])
