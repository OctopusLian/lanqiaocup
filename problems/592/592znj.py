import os
import sys

# 遍历字符统计法

# 定义统计变量
a = 0
# 遍历拿到1-2020中每个数字统计指定的字符数进行累加
for i in range(1,2021):
  # 每个数字先转字符串然后进行统计字符2的数量，赋值给统计变量
  a += str(i).count('2')
print(a)