"""
快速幂
"""


def fastPow(a, n, mod):
    ans = 1
    while n:
        if (n & 1):  ans = ans * a
        a = a * a
        n >>= 1
    return ans % mod


b, p, k = map(int, input().split())
print(fastPow(b, p, k))
