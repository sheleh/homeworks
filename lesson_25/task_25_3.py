# Implement a queue using a singly linked list.

from lesson_25.task_25_1 import Node


class Queue:
    def __init__(self):
        self._head = self._tail = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def enqueue(self, item):
        current = Node(item)
        if self._tail is None:
            self._head = self._tail = current
            return
        self._tail.set_next(current)
        self._tail = current

    def dequeue(self):
        current = self._head
        self._head = current.get_next()

    def display(self):
        current = self._head
        if self.is_empty():
            print('Nothing in queue')
        else:

            rep = f'head = {self._head.get_data()} tail =  {self._tail.get_data()} -> \n'
            while current is not None:
                rep += f'{current.get_data()} -> '
                current = current.get_next()
            return rep


my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)
my_queue.enqueue(20)
my_queue.enqueue(25)
my_queue.dequeue()
print(my_queue.is_empty())
print(my_queue.display())
