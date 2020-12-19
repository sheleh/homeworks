#Mathematician
#Implement a class Mathematician which is a helper class for doing math operations on lists
#The class doesn't take any attributes and only has methods:
#square_nums (takes a list of integers and returns the list of squares)
#remove_positives (takes a list of integers and returns it without positive numbers
#filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
#class Mathematician:
#    pass

#m = Mathematician()

#assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

#assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

#assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, l):
        self.l = l
        self.res = []
        for i in self.l:
            self.res.append(i**2)
        print(f'{self.l} == {self.res}')
    def remove_positives(self,l):
        self.l = l
        self.res = []
        for i in l:
            if i < 0:
                self.res.append(i)
        print(f'{self.l} == {self.res}')
    def filter_leaps(self,l):
        self.l = l
        self.res = []
        for i in l:
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                self.res.append(i)

        print(f'{self.l} == {self.res}')


m = Mathematician()
m.square_nums([7, 4, 6,7 ])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 1600, 2000, 2003, 2020, 1900])