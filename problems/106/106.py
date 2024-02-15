"""
正则问题
"""

s = input().strip()
pos, length = 0, len(s)


def dfs():
    global pos, length
    ans, temp = 0, 0
    while pos < length:
        if s[pos] == '(':
            pos += 1
            temp = temp + dfs()
        elif s[pos] == 'x':
            pos += 1
            temp += 1
        elif s[pos] == '|':
            pos += 1
            ans = max(ans, temp); temp = 0
        elif s[pos] == ')':
            pos += 1
            return max(ans, temp)
    return max(ans, temp)


print(dfs())
