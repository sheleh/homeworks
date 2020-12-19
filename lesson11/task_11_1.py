#School
#Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.


class Person:
    def __init__(self, gender, name, age, height, weight):
        self.gender = gender
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def bmi(self):
        res = self.weight / ((self.height/100)**2)
        if res < 25:
            print(f'{self.name}\'s weight is normal')
        elif 25 < res <= 29:
            print(f'{self.name}\'s have overweight')
        elif res > 30:
            print(f'{self.name}\' Obese')
        return res
class Teacher(Person):
    def __init__(self, gender, name, age, height, weight, salary):
        super().__init__(gender, name, age, height, weight)
        self.salary = salary
    def going_to_job(self):
        print(f'Teacher {self.name} going to work and maybe will have a salary {self.salary}')
class Student(Person):
    def __init__(self, gender, name, age, height, weight, class_num, class_literal):
        super().__init__(gender, name, age, height, weight)
        self.class_num = class_num
        self.class_literal = class_literal
    def going_to_study(self):
        print(f'Student {self.name} going to study in class = {str(self.class_num) + self.class_literal}')


alex = Teacher('male', 'Alex', 35, 185, 77, 3500)
alex.bmi()
alex.going_to_job()
donald = Student('male', 'Donald', 17, 180, 74, 11, 'B')
donald.bmi()
donald.going_to_study()