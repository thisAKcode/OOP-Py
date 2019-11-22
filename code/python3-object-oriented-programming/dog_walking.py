# walk() method to both the Pets and Dog classes
# when you call the method on the Pets class, 
# each dog instance assigned to the Pets class will walk().

#Parent class
class Pets():
    dogs = [] # class attribute
    def __init__(self, dogs):
        self.dogs = dogs
        # simply make an iteration through dogs then call method from Dog()
    def walk(self, action):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True #instance attribute default set to True
        

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    # instance method 
    def eat(self):
        self.is_hungry = False
    # instance method NOTICE there is the same in pets class
    def walk(self):
        return "{} is walking!".format(self.name)
        
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
# create instances of dogs in a global scope
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
    ]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output

