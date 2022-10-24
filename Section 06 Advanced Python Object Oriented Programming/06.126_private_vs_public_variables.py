# Private vs Public Variables
# There is no way to make a method or attribute private in Python.  As a convention programmers use the "_" method
# to tell other programmers that the attribute or method should not be changed.
# To show a attribute should be private use self._name instead of self.name

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name='anonymous', age=0):
        self._name = name  # Attributes
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter('Nathan', 46)
player1.name = '!!!'
player1.speak = 'BOOO'

print(player1.speak)
