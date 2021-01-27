#Extend UnorderedList

#Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method,
# which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going up to but not including the stop position.
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    # get value form node
    def get_data(self):
        return self._data

    # get next node reference
    def get_next(self):
        return self._next

    # set value to node
    def set_data(self, data):
        self._data = data

    # set next node reference
    def set_next(self, new_next):
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
        if self._tail is None:
            self._tail = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            # удаляем первый узел
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        node = Node(item)
        # If the Linked List is empty, then make the new node as head
        if self._head is None:
            self._head = node
            return
        #if self._tail is None:
        #    self._tail = node
        #    return

        current = self._head
        prev = None
        while current is not None:
            prev = current
            current = current.get_next()
        prev.set_next(node)

        #current = self._tail
        #current.set_next(node)
        #self._tail = node
    def index(self, item):
        if self._head is None:
            return False
        current = self._head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            else:
                current = current.get_next()
            pos += 1

    def pop(self, item=-1):
        if self._head is None:
            return False
        previous = None
        current = self._head
        while current is not None:
            if current.get_data() == item:
                break
            if item == -1 and current.get_next() is None:
                previous.set_next(None)
                return current.get_data()
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self._head = current.get_next()
        else:
            try:
                previous.set_next(current.get_next())
                return current.get_data()
            except AttributeError:
                return 'Item not found'


    def insert(self, pos, item):
        current = self._head
        previous = None
        index = 0
        temp = Node(item)
        while current is not None and index < pos:
            previous = current
            current = current.get_next()
            index += 1
        if pos == 0:
            temp.set_next(self._head)
            self._head = temp
        else:
            if current is None:
                previous.set_next(temp)
            else:
                temp.set_next(current)
                previous.set_next(temp)

    def slice(self, start, stop):  # BETA
        current = self._head
        pos = 0
        tmp_slice = UnorderedList()
        while current is not None and pos <= stop:
            if pos >= start and pos < stop:
                item = current.get_data()
                tmp_slice.append(item)
            current = current.get_next()
            pos += 1
        return tmp_slice

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} -> "
            current = current.get_next()
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)


    print(my_list)
    print(my_list.size())
    #print(my_list.search(93))
    #print(my_list.size())
    my_list.remove(93)
    #print(my_list.search(93))
    my_list.append(657)
    my_list.add(115566)
    my_list.append('tail')
    my_list.append(676767)


    print(my_list)
    print(my_list.index(26))

    print(my_list)
    my_list.insert(1, 99)
    my_list.add('head')

    print(my_list)
    #print(my_list.slice(0, 3))
    print(f'pop {my_list.pop()}')
    print(my_list)
    print(f'pop {my_list.pop(115566)}')
    print(f'pop {my_list.pop()}')
    print(f'pop {my_list.pop(98765)}')


    my_list.append('llllast')
    print(my_list)
    res = my_list.slice(0, 2)
    print(res)
