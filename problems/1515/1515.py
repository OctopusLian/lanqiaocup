"""
阶乘计算
https://www.lanqiao.cn/problems/1515/learning/?page=1&first_category_id=1&problem_id=1515

"""

n = int(input())
ans = 1
for i in range(1, n + 1):
    ans *= i
print(ans)