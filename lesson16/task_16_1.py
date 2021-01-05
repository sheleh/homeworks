#Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function
iterable = ['one', 'two', 'three', 'four', 'five']

def with_index(iterable, start=1):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

print(list(with_index(iterable)))


class With_Index:
    def __init__(self, data, start = 0):
        self.data = data
        self.index = start
        self.res = ''
    def __iter__(self):
        return self
    def __next__(self):
        if self.index > (len(self.data)):
            raise StopIteration
        else:
            self.res = self.index, self.data[self.index-1]
            self.index += 1
            return self.res  ### Почему не работает yield?(бесконечный цикл)

print(list(With_Index(iterable)))