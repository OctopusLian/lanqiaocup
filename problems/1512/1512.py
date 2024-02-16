"""
https://www.lanqiao.cn/problems/1512/learning/?page=1&first_category_id=1&problem_id=1512
汉诺塔
"""

def hanoi(x, y, z, n):
    global sum
    if n == 1:
        sum += 1
        if (sum == m):  print(f"#{n}: {x}->{z}")
    else:
        hanoi(x, z, y, n - 1)
        sum += 1
        if sum == m:    print(f"#{n}: {x}->{z}")
        hanoi(y, x, z, n - 1)


n, m = map(int, input().split())
sum = 0
hanoi('A', 'B', 'C', n)
print(sum)
