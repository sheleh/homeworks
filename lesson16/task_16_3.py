#Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
data = ['London', 'New York', 'Alabama', 'Moscow', 'Delhi', 'Beijing']


class Sq_Brackets:
    def __init__(self, names_):
        self.data = names_
        self.index = 0
        self.res = ''

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == (len(self.data)):
            raise StopIteration
        else:
            self.res = '[' + self.data[self.index] + ']'
            self.index += 1
            return self.res



for i in Sq_Brackets(data):
    print(i)


