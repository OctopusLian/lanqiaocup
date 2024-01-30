"""
刷题统计
https://www.lanqiao.cn/problems/2098/learning/?page=1&first_category_id=1&problem_id=2098

思路：

"""
import os
import sys

# 请在此输入您的代码
# 接收命令行输入
#//是除，无小数部分，如7//2  结果为3     /结果为3.5
#%为求余数，如7除3=2余1，结果为1

a,b,n = map(int,input().split())
week = a*5 + b*2  #计算一周总的做题数
days = (n//week)*7#做了几个整周的天数
n %= week         #剩余的题数
if n <= 5*a:      #如果剩余的题数，五天能做完
    days += n//a + (0 if n % a == 0 else 1)
    #天数+= 如果剩余的题数做x(n//a)天，每天做a道做完,后面的三目运算返回0天，如果还有没做完的，再加1天
else:    #如果剩余的题数,五天做不完，剩余两天能做完
    days += 5     #加上之前的五天
    n -= 5*a      #减去五天的做题数
    days += n//b + (0 if n % b == 0 else 1)
    #天数+= 如果剩余的题数做x(n//b)天，每天做b道做完,后面的三目运算返回0天，如果还有没做完的，再加1天
print(days)