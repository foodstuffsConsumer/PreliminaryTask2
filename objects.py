class Player:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def loseHealth(self, healthLoss):
        self.health -= healthLoss
        if self.health <= 0:
            print("AND THEY'RE DEAAAAAAD!")
            quit()

    def gainHealth(self, healthGain):
        self.health += healthGain
        print(f"{self.name} heals for {healthGain} HP!")

    def gainAttack(self, attackGain):
        self.attack += attackGain
        print(f"{self.name} increases their ATK by {attackGain}!")

    def dealDamage(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")
        target.loseHealth(self.attack)


class Enemy:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def loseHealth(self, healthLoss):
        self.health -= healthLoss
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def dealDamage(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")
        target.loseHealth(self.attack)

    def groan(self):
        print(f"{self.name} groans in pain...")

class Goblin(Enemy):
    def eatMeat(self, healthGain):
        self.health += healthGain
        print(f"{self.name} chomps on a piece of meat, healing themself for {healthGain} HP!")

class Barbarian(Enemy):
    def warCry(self, attackBuff):
        self.attack += attackBuff
        print(f"{self.name} lets out a war cry, bolstering their strength by {attackBuff}!")

class Alchemist(Enemy):
    def debuffPlayer(self, target, attackDebuff):
        target.attack -= attackDebuff
        print(f"{self.name} splashes a potion onto {target.name}, weakening their strength by {attackDebuff}!")