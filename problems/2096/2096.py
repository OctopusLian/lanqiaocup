"""
https://www.lanqiao.cn/problems/2096/learning/?page=1&first_category_id=1&problem_id=2096
小明特别喜欢顺子。
顺子指的就是连续的三个数字:123、456 等。顺子日期指的就是在日期的 yyyymmdd 表示法中，存在任意连续的三位数是一个顺子的日期。
例如 20220123 就是一个顺子日期，因为它出现了一个顺子:123;而20221023则不是一个顺子日期，它一个顺子也没有。小明想知道在整个 2022年份中，一共有多少个顺子日期?
"""

import os
import sys

# 请在此输入您的代码
res = 0
for month in range(1,13):
    for day in range(1,32):
        # 构建类似 20220123 这样的日期
        s = "2022%02d%02d" % (month,day)
        if "012" in s or "123" in s :
            res += 1
print(res) # 14
