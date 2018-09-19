class Stack(object):
    """
    模拟栈
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    # 返回栈顶的元素，并删除它
    def pop(self):
        return self.items.pop()

    # 返回栈顶的元素，并不删除它
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


"""
一个典型的站应用就是十进制转换为二进制
"""


def decimal_to_bin(num):
    stack = Stack()
    cur = num
    while cur > 0:
        rem = cur % 2
        cur = cur // 2
        stack.push(rem)
    binstr = ''
    while not stack.isEmpty():
        binstr += str(stack.pop())

    return binstr


if __name__ == '__main__':
    print(decimal_to_bin(10))