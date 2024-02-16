"""
FBI 树
"""


def build_FBI(p, left, right):
    if left == right:
        if s[right] == '1':
            tree[p] = 'I'
        else:
            tree[p] = 'B'
        return
    mid = (left + right) // 2
    build_FBI(2 * p, left, mid)
    build_FBI(2 * p + 1, mid + 1, right)

    if tree[2 * p] == 'B' and tree[2 * p + 1] == 'B':
        tree[p] = 'B'
    elif tree[2 * p] == 'I' and tree[2 * p + 1] == 'I':
        tree[p] = 'I'
    else:
        tree[p] = 'F'


def postorder(p):
    if tree[2 * p] != '':  postorder(2 * p)
    if tree[2 * p + 1] != '':   postorder(2 * p + 1)
    print(tree[p], end='')


n = int(input())
s = input()
tree = [''] * 4400
build_FBI(1, 0, len(s) - 1)
postorder(1)
