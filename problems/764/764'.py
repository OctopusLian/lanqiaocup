"""
一元三次方程求解
"""

n = input().split()
a, b, c, d = eval(n[0]), eval(n[1]), eval(n[2]), eval(n[3])


def y(x):
    return a * x * x * x + b * x * x + c * x + d


for i in range(-100, 100):
    left = i
    right = i + 1
    y1 = y(left)
    y2 = y(right)
    if y1 == 0:
        print("{:.2f}".format(left), end=" ")
    if y1 * y2 < 0:
        while (right - left) >= 0.001:  # eps=0.001
            mid = (left + right) / 2
            if y(mid) * y(right) <= 0:
                left = mid
            else:
                right = mid
        print("{:.2f}".format(right), end=" ")
