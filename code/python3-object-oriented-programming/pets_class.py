# "Dog inheritance" overriding functionality 
'''Create a Pets class that holds instances of dogs;
this class is completely separate from the Dog class. 
In other words, the Dog class does not inherit 
from the Pets class. Then assign three dog instances 
to an instance of the Pets class'''

'''desired output

I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course.

'''
#Parent class
class Pets():
    dogs = [] # class attribute
    def __init__(self, dogs):
        self.dogs = dogs
        
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

# instantiate the Pets class
my_pets = Pets(my_dogs)

# output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat() # NOTICE  a way to feed each dog
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True
# output about hunger
if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry")