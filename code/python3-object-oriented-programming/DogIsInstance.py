#  isinstance() determines if an instance is also an inst of a 
# certain parent class

class Dog:
    
    # class attr
    species = 'mammal'
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)    

# child class inherits from Dog() class
class RussellTerrier(Dog):
    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)
    
# Child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# Child classes inherit attributes and 
# behaviours from the parent class
jim = Bulldog("Jim", 12)
print(jim.description()) # use parent class instance method

# child classes have specific attributes
# and behaviours as well
print(jim.run('slowly'))

# is jim an instance of a Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier('Johnny Walker',4)
print(isinstance(johnnywalker, Bulldog))

# print(isinstance(julie, jim)) # jim is an instance rather than a class
