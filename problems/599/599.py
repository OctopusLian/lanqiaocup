"""
平方和
https://www.lanqiao.cn/problems/599/learning/?page=1&first_category_id=1&problem_id=599

思路：
声明一个total int类型变量
遍历1-2019之间的数字
将遍历的每一个数字转为字符串
判断 '2' '0' '1' '9'这4个字符是否在这个字符串中
如果在，就将这个数先平方，然后和total相加
最后输出total的值
"""
import os
import sys

ans=0
for i in range(1,2020):
  for a in str(i):
    if a in '2019':
      ans+=i*i
      break
print(ans)

# 请在此输入您的代码

