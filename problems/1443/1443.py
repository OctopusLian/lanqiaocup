"""
编程作业
"""

N = 1000006
Next = [0] * N
slen, plen = 0, 0
s = [0] * N
p = [0] * N
pre = [0] * 29


def check(a, b, j):
    if a < 0 or b < 0: return a == b
    return a == b or (b == 0 and a > j)


def inits():
    global pre, slen
    pre = [0] * 29  # 清空
    v = ' ' + input()
    slen = len(v) - 1
    for i in range(1, slen + 1):
        if v[i] >= 'A' and v[i] <= 'Z':
            s[i] = -ord(v[i])  # 字符不能直接相减，需要用ord()
        else:
            if pre[ord(v[i]) - ord('a') + 1] > 0:
                s[i] = i - pre[ord(v[i]) - ord('a') + 1]
            else:
                s[i] = 0
            pre[ord(v[i]) - ord('a') + 1] = i


def initp():
    global pre, plen
    pre = [0] * 29
    v = ' ' + input()
    plen = len(v) - 1
    for i in range(1, plen + 1):
        if v[i] >= 'A' and v[i] <= 'Z':
            p[i] = -ord(v[i])
        else:
            if pre[ord(v[i]) - ord('a') + 1] > 0:
                p[i] = i - pre[ord(v[i]) - ord('a') + 1]
            else:
                p[i] = 0
            pre[ord(v[i]) - ord('a') + 1] = i


def getNext():
    for i in range(1, plen):
        j = Next[i];
        while j > 0 and check(p[i + 1], p[j + 1], j) == 0:   j = Next[j]
        if check(p[i + 1], p[j + 1], j) > 0:
            Next[i + 1] = j + 1
        else:
            Next[i + 1] = 0


def kmp():
    ans = 0
    j = 0
    for i in range(0, slen):
        while j > 0 and check(s[i + 1], p[j + 1], j) == 0:  j = Next[j]
        if check(s[i + 1], p[j + 1], j) > 0:   j += 1
        if j == plen:
            ans += 1
            j = Next[j]
    print(ans)


Q = int(input())
for i in range(Q):  inits();  initp();  getNext();  kmp()
