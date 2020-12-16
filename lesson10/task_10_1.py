#A Person class
#Make a class called Person. Make the __init__() method take firstname, lastname,
# and age as parameters and add them as attributes. Make another method called talk()
# which makes prints a greeting from the person containing, for example like this: “Hello,
# my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.age = age
    def talk(self):
        print(f'my name is {self.firstname} {self.lastname} and I’m {self.age} years old')
user1 = Person('bob', 'marley', 36)
user1.talk()
