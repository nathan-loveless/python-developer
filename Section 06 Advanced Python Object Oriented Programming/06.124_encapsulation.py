# Encapsulation

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name='anonymous', age=0):
        self.name = name  # Attributes
        self.age = age

    # def run(self):
    #     print('run')
    #
    # def speak(self):
    #     print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('Nathan', 46)
print(player1.name)
print(player1.age)

player1.age = 100

print(player1.age)
