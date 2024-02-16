"""
小明的字符串
"""

N = 1000005
Next = [0] * N


def getNext(p):  # 计算Next[1]~Next[plen]
    for i in range(1, len(p)):
        j = Next[i];  # j的后移：j指向前缀阴影w的后一个字符
        while j > 0 and p[i] != p[j]:  # 阴影的后一个字符不相同
            j = Next[j]  # 更新j
        if p[i] == p[j]:
            Next[i + 1] = j + 1
        else:
            Next[i + 1] = 0


def kmp(s, p):
    ans = 0
    j = 0
    for i in range(0, len(s)):
        while j > 0 and s[i] != p[j]:  # 失配了。注意j==0是情况(1)
            j = Next[j]  # j滑动到Next[j]位置
        if s[i] == p[j]:  # 当前位置的字符匹配，继续
            j += 1
            ans = max(ans, j)  # 去掉这一句，本代码就是最基本的KMP
        if j == len(p): return ans  # j到了P的末尾，找到了一个匹配
    return ans  # 返回p在s中出现的最长前缀


s = input()
t = input()
getNext(t)
print(kmp(s, t))
