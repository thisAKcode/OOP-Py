# child class override attributes 
# and behaviours from the parent class
class Dog:
    species = 'mammal'

# child 1 
class SomeBreed(Dog): #  inherits the species
    pass
# child 2
class SomeOtherBreed(Dog): # overrides the species,
    species = 'reptile' #  setting it to reptile.

frank = SomeBreed()
print(frank.species)

beans = SomeOtherBreed()
print(beans.species)