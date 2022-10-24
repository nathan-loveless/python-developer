# @classmethod and @staticmethod

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name='anonymous', age=0):
        self.name = name  # Attributes
        self.age = age

    def shout(self):  # Methods
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    # You don't have access to cls as you do with @classmethod
    @staticmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


# player1 = PlayerCharacter('Tom', 20)
player3 = PlayerCharacter.adding_things(2, 3)

print(player3.age)
