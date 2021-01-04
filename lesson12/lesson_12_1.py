#Method overloading.
#Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
# and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’,
# while Cat’s can be to print ‘meow’.
#Also, create a simple generic function, which takes as input instance of a Cat or Dog
# classes and performs talk method on input parameter.

class Animal:

    def __init__(self, name):
        self.name = name

    # Abstract method
    def talk(self):
        raise NotImplementedError('Must be implemented')

    #def dif_talk(self, msg):
    #    self.msg = str(msg)
    #    print(f'{self.name} says abnormal talk like * {self.msg} *')


class Cat(Animal):
    def talk(self):
        print(f'{self.name} say MeowMeowMeow!')


class Dog(Animal):
    def talk(self):
        print(f'{self.name} say WoofWoofWoof!')

cat1 = Cat('Murka')
cat1.talk()
dog1 = Dog('Barbos')
dog1.talk()

# simple generic function
def different_talk(animal,dif_talks):
    dif_talks = str(dif_talks)
    print(f'{animal.name} will say * {dif_talks} *')

different_talk(cat1,'Im a cat')
#dog1.dif_talk('Where is my Money?!')