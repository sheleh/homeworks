# Task 1
# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self):
        self._items = []
        self.rev_res = ''

    def is_empty(self):  # тут момент
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def show_rev(self):
        while not self.is_empty():
            self.rev_res += self.pop()
        return self.rev_res


data = 'Logic will get you from A to B. Imagination will take you anywhere. Albert Einstein'


def make_reverse(str_: str):
    res = Stack()
    for value in str_:
        res.push(value)
    print(str_)
    print(res.show_rev())


if __name__ == '__main__':
    try:
        make_reverse(data)
    except Exception:
        print('OOOPS')
