class Queue(object):

    """
    实现队列
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise KeyError('the queue is empty')
        self.items.pop(0)