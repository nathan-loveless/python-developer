# Inheritance 2
# If you don't have any attributes to assign __init__ is called automatically


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left -  {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)

print(isinstance(wizard1, User))
