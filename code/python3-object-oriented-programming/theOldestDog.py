'''
content 
instantiate, instance methods, 
object inheritance
'''
class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def description(self):
        return '{} is {} years old'.format(self.name, self.age)
    # instance method to add behavior
    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)
philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)
titus = Dog('Titus', 7)

# call instance methods
print(mikey.description()) # notice that (mikey.description) is not an option
print(mikey.speak('Gruff Gruff'))

# define outside method
def get_the_biggest_num(*args):
    return max(args)

# give an output
print('The oldest dog is {} years old.'.format(
get_the_biggest_num(philo.age, mikey.age, titus.age)))
    
