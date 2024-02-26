xdir = [-2, -1, 1, 2, 1, -1]
ydir = [0, 1, 1, 0, -1, -1]


def walk(d, q, x, y):
    x += xdir[d] * q
    y += ydir[d] * q
    return x, y


d1, p1, q1, d2, p2, q2 = map(int, input().split())
x1, y1 = walk(d1, p1, 0, 0)
x1, y1 = walk((d1 + 2) % 6, q1, x1, y1)
x2, y2 = walk(d2, p2, 0, 0)
x2, y2 = walk((d2 + 2) % 6, q2, x2, y2)
dx, dy = abs(x1 - x2), abs(y1 - y2);

if dx >= dy:
    print((dx + dy) // 2)  # 先横走，再斜着走
else:
    print(dy)  # 一直斜着走
