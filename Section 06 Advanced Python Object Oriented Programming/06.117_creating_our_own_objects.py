# Creating our own objects

class PlayerCharacter:
    # Also called constructor method
    def __init__(self, name, age):
        self.name = name  # Attributes
        self.age = age

    def run(self):  # Methods
        print('run')
        return 'done'


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.run())
print(player2.age)
