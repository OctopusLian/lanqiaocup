"""
垒骰子
"""

MOD = int(1e9 + 7)  # 注意一定要用int转换


def multi(A, B):  # 矩阵乘法
    C = [[0] * 6 for i in range(6)]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                C[i][j] = int((C[i][j] + A[i][k] * B[k][j]) % MOD)
    return C


def power(A, n):  # 矩阵快速幂
    res = [[0] * 6 for i in range(6)]
    for i in range(6):  res[i][i] = 1
    while n:
        if n % 2:   res = multi(res, A)
        A = multi(A, A)
        n >>= 1
    return res


def solve(n, dice):
    transfer = [[4] * 6 for i in range(6)]  # 转移矩阵
    for i in range(6):  # 去掉互斥的情况
        for j in dice.get((i + 3) % 6, []):  # 0对面是3，1对4，2对5
            transfer[i][j] = 0
    transfer = power(transfer, n - 1)  # 转移矩阵乘n-1次
    temp = [4] * 6  # 表示最下面的骰子
    ans = [0] * 6
    for i in range(6):  # 最后乘最下面的骰子
        for j in range(6):
            ans[i] += transfer[i][j] * temp[j]
    print(int(sum(ans) % MOD))


n, m = [int(str) for str in input().split()]
dice = dict()  # 用字典记录互相排斥的面
for i in range(m):
    x, y = [int(str) - 1 for str in input().split()]
    if x not in dice:
        dice[x] = [y]
    else:
        dice[x].append(y)
    if y not in dice:
        dice[y] = [x]
    else:
        dice[y].append(x)
solve(n, dice)
