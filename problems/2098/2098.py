"""
刷题统计
https://www.lanqiao.cn/problems/2098/learning/?page=1&first_category_id=1&problem_id=2098

思路：

"""
import os
import sys

# 请在此输入您的代码
# 接收命令行输入
input_str = input("请输入值，以空格分隔：")
# 通过空格分隔输入的值，并转换为整数类型
input_list = [int(x) for x in input_str.split()]

a = input_list[0]
b = input_list[1]
n = input_list[2]

total = 0
totalDay = 0

day = 0

while total < n:
    if day > 5:
        total += b
        if day == 7:
            day = 0
    else:
        total += a

    day += 1
    totalDay += 1

print(totalDay)
