# Attributes and Methods

class PlayerCharacter:
    membership = True  # Class object attribute.  Can use self or PlayerCharacter

    # Also called constructor method
    def __init__(self, name, age):
        if self.membership:
            self.name = name  # Attributes
            self.age = age

    def shout(self):  # Methods
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.run('hello'))
print(player2.membership)
