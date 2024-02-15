"""
技能升级
"""


def check(mid):  # 最后一次技能升级，最多能不能到mid
    cnt = 0
    for i in range(n):
        if a[i] < mid:
            continue  # 第i个技能的初值还不够mid，不用这个技能
        cnt += (a[i] - mid) // b[i] + 1  # 第i个技能用掉的次数
        if cnt >= m:
            return True  # 所有技能升级总次数大于等于m次，说明mid设小了
    return False  # 所有技能升级总次数小于m次，说明mid设大了


n, m = map(int, input().split())
a = []  # 存ai
b = []  # 存bi
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
L, R = 1, 1000000  # 二分枚举最后一次攻击力最高能加多少
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        L = mid + 1  # 增加mid
    else:
        R = mid - 1  # 减小mid
attack = 0
cnt = m
for i in range(n):
    if a[i] < R:
        continue
    t = (a[i] - L) // b[i] + 1  # 第i个技能升级次数
    if a[i] - b[i] * (t - 1) == R:
        t -= 1  # 这个技能每次升级刚好等于R，其他技能更好
    attack += (a[i] * 2 - (t - 1) * b[i]) * t / 2
    cnt -= t
print(int(attack) + cnt * R)