"""
迷宫
注意本题是填空题。下面代码直接提交到oj，“答案错误”。自己运行得到答案后，再把答案提交到OJ。
"""

from queue import Queue


def print_path(x, y):
    if x == 1 and y == 1:
        return  # 回溯到了起点，递归结束，返回
    if pre[x][y] == 'D':
        print_path(x - 1, y)  # 回溯，往上 U
    if pre[x][y] == 'L':
        print_path(x, y + 1)  # 回溯，往右 R
    if pre[x][y] == 'R':
        print_path(x, y - 1)
    if pre[x][y] == 'U':
        print_path(x + 1, y)
    print(pre[x][y], end="")  # 最后打印的是终点


mp = []
for i in range(0, 30):
    mp.append(input())  # 读迷宫
for i in range(len(mp)):
    mp[i] = '1' + mp[i] + '1'  # 为迷宫加左边和右边的围墙
mp = [52 * '1'] + mp + [52 * '1']  # 为迷宫加上面和下面的围墙
vis = [list(map(int, list(i))) for i in mp]  # 记录迷宫的状态
k = ('D', 'L', 'R', 'U')  # 方向，定义为元组，不可改
dir = ((1, 0), (0, -1), (0, 1), (-1, 0))
pre = [[(-1, -1)] * 52 for i in range(32)]  # 用于保存前一个点

# 下面是bfs:
vis[1][1] = 1  # 起点是(1,1),终点是(30,50)
q = Queue()
q.put((1, 1))
while q.qsize() != 0:  # 以（1，1）为起点开始移动
    now = q.get()
    if now[0] == 30 and now[1] == 50:
        print_path(30, 50)
        exit
    for i in range(4):
        x = now[0] + dir[i][0]
        y = now[1] + dir[i][1]
        if vis[x][y] != 1:  # 把访问过的点变成墙，后面不再访问
            vis[x][y] = 1
            pre[x][y] = k[i]
            q.put((x, y))
