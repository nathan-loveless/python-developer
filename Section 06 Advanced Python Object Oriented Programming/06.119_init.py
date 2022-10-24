# __Init__

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # Attributes
            self.age = age

    def shout(self):  # Methods
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Tom', 10)

print(player1.shout())
