# Abstraction
# Useful because it allows you to use a method of a class without having to know internally how it operates or
# is implemented

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name='anonymous', age=0):
        self.name = name  # Attributes
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')
        player1.name = '!!!'
        player1.speak = 'BOOO'


player1 = PlayerCharacter('Nathan', 46)
player1.speak()

print(player1.speak)
