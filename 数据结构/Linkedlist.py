class Node(object):
    '''
    data 保存节点的数据
    next 保存下一个节点对象
    '''

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        # 输入头节点， 返回链表的长度
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def append(self, data):
        # 若数据为空 ，则返回 None
        if data is None:
            return None

        # 若头节点为空，直接将输入数据作为头节点
        node = Node(data)
        if self.head is None:
            self.head = node
            return node

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    # 查找某个节点，时间复杂度为 O(n)
    def search(self, data):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return curr_node

    def getIndex(self, data):
        curr_node = self.head
        i = 0
        while curr_node is not None:
            if curr_node.data == data:
                return i
            curr_node = curr_node.next
            i += 1

        return '这个数不存在'


if __name__ == '__main__':
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node1.next = node2
    # node2.next = node3
    # node = node1
    # while node:
    #     print(node.data)
    #     node = node.next

    linklist = LinkedList()
    for i in range(9):
        linklist.append(i)
    print(linklist.__len__())
    print(linklist.getIndex(9))