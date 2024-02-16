"""
点和线段关系
"""


def Cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2  # 叉积


def Dot(x1, y1, x2, y2):
    return x1 * y2 + y1 * x2  # 点积


t = int(input())
for _ in range(t):
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    cx, cy = map(float, input().split())
    x1 = ax - bx
    y1 = ay - by
    x2 = ax - cx
    y2 = ay - cy
    if Cross(x1, y1, x2, y2) == 0 and Cross(x1, y1, x2, y2) <= 0:
        print('Yes')
    else:
        print('No')
