"""
https://www.lanqiao.cn/problems/174/learning/?page=1&first_category_id=1&problem_id=174
付账问题
"""

from math import *

n, s = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
avg = s / n
sum = 0
for i in range(n):
    if a[i] * (n - i) < s:
        sum += pow(a[i] - avg, 2)
        s -= a[i]
    else:
        cur_avg = s / (n - i);  # 更新平均出钱数
        sum += pow(cur_avg - avg, 2) * (n - i)
        break
print("{:.4f}".format(sqrt(sum / (n))))
