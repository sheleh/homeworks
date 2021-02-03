# Implement a stack using a singly linked list.
from task_25_1 import Node


class Stack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def push(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            return
        else:
            current = node
            current.set_next(self._head)
            self._head = current

    def pop(self):
        if self._head is None:
            return False
        current = self._head
        self._head = current.get_next()
        return current.get_data()

    def peek(self):
        if self._head is None:
            return False
        return self._head.get_data()

    def display(self):
        current = self._head
        if self.is_empty():
            print('Nothing in Stack')
        else:
            rep = '-> '
            while current is not None:
                rep += f'{current.get_data()} -> '
                current = current.get_next()
            return rep


if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(99)
    my_stack.push(45)
    my_stack.push(33)
    my_stack.push(22)

    print(my_stack.is_empty())
    print(my_stack.display())
    print(my_stack.pop())
    print(my_stack.display())
    print(my_stack.peek())
