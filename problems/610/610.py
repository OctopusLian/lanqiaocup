"""
https://www.lanqiao.cn/problems/610/learning/?page=1&first_category_id=1&problem_id=610
分数
2018年第九届蓝桥杯C/C++大学A组，Java大学A组
"""

# 请在此输入您的代码
a, b = 1, 0
for i in range(0, 20):
    b += a
    a *= 2
print("%d/%d" % (b, a / 2))
