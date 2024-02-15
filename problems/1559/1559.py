"""
分解质因数
"""


def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return i
    return x


a, b = map(int, input().split())
for x in range(a, b + 1):
    print(f"{x}=", end="")
    while x != 1:
        ans = f(x)
        if x / ans != 1:
            print(f"{ans}*", end="")
        else:
            print(f"{int(ans)}")
        x /= ans
