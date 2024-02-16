"""
跳蚱蜢
"""


def insertQueue(q: list, dir: int, news: tuple, vis: set):
    pos = news[1]
    status = news[0]
    insertPos = (pos + dir + 9) % 9
    t = list(status)
    t[pos], t[insertPos] = t[insertPos], t[pos]
    addStatus = "".join(t)
    if addStatus not in vis:
        vis.add(addStatus)
        q.append((addStatus, insertPos, news[2] + 1))


q = [("012345678", 0, 0)]
vis = set()
vis.add("012345678")
while q:
    news = q.pop(0)
    if news[0] == "087654321":  # 到达了目标状态，输出最少步数
        print(news[2])
        break
    insertQueue(q, -2, news, vis)  # 扩展下一层的4种情况
    insertQueue(q, -1, news, vis)
    insertQueue(q, 1, news, vis)
    insertQueue(q, 2, news, vis)
