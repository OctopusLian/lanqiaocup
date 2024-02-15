def check1(x1, x2, x3):
    if x1 >= x2 and x1 >= x3:
        if x1 == x2 + x3 and a[2] + a[3] - x2 == a[4] + a[5] - x3:
            return True
    if x2 >= x1 and x2 >= x3:
        if x2 == x1 + x3 and a[0] + a[1] - x1 == a[4] + a[5] - x3:
            return True
    if x3 >= x1 and x3 >= x2:
        if x3 == x1 + x2 and a[0] + a[1] - x1 == a[2] + a[3] - x2:
            return True
    return False


def check2(x1, x2, x3):
    if x1 >= x2 and x1 >= x3:
        if x1 == x2 + x3:
            return True
    if x2 >= x1 and x2 >= x3:
        if x2 == x1 + x3:
            return True
    if x3 >= x1 and x3 >= x2:
        if x3 == x1 + x2:
            return True
    return False


T = int(input())
for t in range(T):
    a = list(map(int, input().split()))
    ans = 8
    for i in range(0, 2):  # 第1个矩形
        for j in range(2, 4):  # 第2个矩形
            for k in range(4, 6):  # 第3个矩形
                x1, x2, x3 = a[i], a[j], a[k]
                if x1 == x2 and x2 == x3:
                    ans = min(ans, 4)
                if check1(x1, x2, x3):
                    ans = min(ans, 4)
                if x1 == x2 or x1 == x3 or x2 == x3:
                    ans = min(ans, 6)
                if check2(x1, x2, x3):
                    ans = min(ans, 6)
    print(ans)
