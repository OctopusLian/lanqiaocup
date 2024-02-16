class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList():
    def __init__(self, node=None):
        self.__head = node

    def left_insert(self, x, y):
        pre = self.__head
        while pre.next.data != x:  pre = pre.next
        node = Node(y)
        node.next = pre.next
        pre.next = node

    def right_insert(self, x, y):
        pre = self.__head
        while pre.data != x:  pre = pre.next
        node = Node(y)
        node.next = pre.next
        pre.next = node

    def print_list(self):
        cur = self.__head
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next


n = int(input())
a = int(input())
node = Node(a)
li = SingleLinkList(node)
for i in range(n - 1):
    x, y, z = map(int, input().split())
    if z == 0:
        li.left_insert(y, x)
    else:
        li.right_insert(y, x)
li.print_list()
