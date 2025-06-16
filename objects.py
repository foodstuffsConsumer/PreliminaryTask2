class Player:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def loseHealth(self, healthloss):
        self.health -= healthloss
        print(self.name + 'has lost' + healthloss + 'health!')
        if self.health >= 0:
            print("AND THEY'RE DEAAAAAAD!")

    def gainHealth(self, healthgain):
        self.health += healthgain
        print(self.name + 'has healed for' + healthgain + 'health!')

class Enemy:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def loseHealth(self, healthloss):
        self.health -= healthloss
        print(self.name + 'has lost' + healthloss + 'health!')
        if self.health >= 0:
            print(self.name + 'has been defeated!')