# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!


class Boss:
    def __init__(self, id_, name, company):
        self.id = int(id_)
        self.name = name.title()
        self.company = company.title()
        self.__workers = []

    def __add_workers(self, new_worker: object):
        self.__workers.append(new_worker)
        new_worker.boss = self
        new_worker.company = self.company

    def _delete_workers(self, value: object):
        self.__workers.remove(value)

    @property
    def get_workers(self):
        """Return list of workers"""
        return self.__workers

    @get_workers.setter
    def get_workers(self, value):
        #self._delete_workers(value) #####
        self.__add_workers(value)

    @get_workers.deleter  # как удалить из списка работников передав значение для удалеиня?
    def get_workers(self):
        pass



    def __str__(self):
        return f'{self.name} / {self.company} / {self.__workers}'

    def __repr__(self):
        return f'{self.name} / {self.company} / {self.__workers}'


class Worker(Boss):

    def __init__(self, id_, name, company, boss):
        super().__init__(id_, name, company)
        if isinstance(boss, Boss):
            self.boss = boss
            print(f'now my boss is {self.boss}')
            self.boss.get_workers = self
        else:
            print('You not my boss, get out')



    def change_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss._delete_workers(self)  # удалямся у текущего босса
            self.boss = new_boss  # меняем босса
            self.boss.get_workers = self  # добавляемся в список работников нового босса

    def __str__(self):
        return f'Worker info : {self.name} / {self.company} / {self.boss.name} \n'

    def __repr__(self):
        return f'Worker info : {self.name} / {self.company} / {self.boss.name} \n'


b1 = Boss(0o2, 'Tim Cook', 'Apple')
b2 = Boss(0o03, 'Bill Gates', 'Microsoft')
w1 = Worker(0o1, 'John', 'Apple', b1)
w2 = Worker(0o4, 'Mary', 'Apple', b1)
w3 = Worker(0o5, 'Vasya', 'Microsoft', b2)
w4 = Worker(0o06, 'Django', 'Freeman', b1)
print('вася ушел в эппл')
w3.change_boss(b1)
print('майкрософт переманил к себе джанго')
w4.change_boss(b2)



#print(w1)
#print(w2)
#print(w3)
#print(b1)
print(f'workers of {b1.name} is: \n{b1.get_workers}')

print(f'workers of {b2.name} is: \n{b2.get_workers}')
#print(w4)
