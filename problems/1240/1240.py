"""
点和直线关系
"""


def Cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2  # 叉积


t = int(input())
for _ in range(t):
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    cx, cy = map(float, input().split())
    x1 = ax - bx
    y1 = ay - by
    x2 = ax - cx
    y2 = ay - cy
    s = Cross(x1, y1, x2, y2) / 2  # 用叉积算面积
    if s > 0:
        print("L")
    if s < 0:
        print("R")
    if s == 0:
        print("IN")
