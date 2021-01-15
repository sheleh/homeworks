#Doggy age
#Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dogs_age):
        self.dogs_age = dogs_age

    def human_age(self, age):
        age *= self.age_factor
        return age


martin = Dog(7)
print(martin.human_age(10))