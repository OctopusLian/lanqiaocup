"""
单词接龙
"""


def check(x, y):
    flag = 0
    for i in range(1, min(len(x), len(y))):
        if x[-i:len(x)] == y[:i]:
            flag = 1
            break
    if flag == 1:
        if x[:len(x) - i] in y[i:] or y[i:] in x[:len(x) - i]:
            return False
        else:
            return i
    else:
        return False


def dfs(dragon, x):
    global ans
    ans = max(len(dragon), ans)
    for i in range(n):
        if check(x, word[i]) != False and vis[i] < 2:
            r = dragon + word[i][check(x, word[i]):]
            vis[i] += 1
            dfs(r, word[i])
            vis[i] -= 1


n = int(input())
word = []
for i in range(n):   word.append(input())
first = input()
ans = 0
for i in range(n):
    vis = [0] * n
    if word[i][0] == first:
        vis[i] += 1
        res = word[i]
        dfs(res, word[i])
print(ans)
