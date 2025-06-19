import time
import random
import objects

player = objects.Player('The Knight', 7, 30, 30)
goblin = objects.Goblin(random.choice(('Krubs', 'Alb', 'Klaank')), 3, 8, 8)
barbarian = objects.Barbarian(random.choice(('Ragnar', 'Korgoth', 'Holfar')), 7, 18, 18)
alchemist = objects.Alchemist(random.choice(('Eloran', 'Orin', 'Mira', 'John Alchemy')), 5, 12, 12)

print(f"You face {goblin.name}, {barbarian.name}, and {alchemist.name}!")

def kickingBodies(victim):
    print(f"{player.name} kicks {victim} while they're down. Jerk.")

def gameStatus():
    print('\n[GAME STATUS]')
    print(f"\n{player.name} (that's you) has {player.health}/{player.maxhp} HP and {player.attack} ATK.")
    print(f"{goblin.name} the {type(goblin).__name__} has {goblin.health}/{goblin.maxhp} HP and {goblin.attack} ATK.")
    print(f"{barbarian.name} the {type(barbarian).__name__} has {barbarian.health}/{barbarian.maxhp} HP and {barbarian.attack} ATK.")
    print(f"{alchemist.name} the {type(alchemist).__name__} has {alchemist.health}/{alchemist.maxhp} HP and {alchemist.attack} ATK.")

    if goblin.health <= 0 and barbarian.health <= 0 and alchemist.health <= 0:
        print(f"\n{player.name} wins the battle!")
        quit()

def playerAttack():

    print("\nWho would you like to attack?")
    print(f"1 - {goblin.name} the {type(goblin).__name__}")
    print(f"2 - {barbarian.name} the {type(barbarian).__name__}")
    print(f"3 - {alchemist.name} the {type(alchemist).__name__}")
    command = input('\nType in a corresponding number... ')

    if command == '1':
        if goblin.health > 0:
            player.dealDamage(goblin)
        else:
            kickingBodies(goblin.name)

    if command == '2':
        if barbarian.health > 0:
            player.dealDamage(barbarian)
        else:
            kickingBodies(barbarian.name)

    if command == '3':
        if alchemist.health > 0:
            player.dealDamage(alchemist)
        else:
            kickingBodies(alchemist.name)

def goblinAction():

    if goblin.health > 0:
        for _ in range(2):
            if goblin.health != goblin.maxhp:
                if random.randint(1, 2) == 1:
                    goblin.eatMeat(2)
                else:
                    goblin.dealDamage(player)
            else:
                goblin.dealDamage(player)
    else:
        goblin.groan()
    time.sleep(1.5)

def barbarianAction():

    if barbarian.health > 0:
        if random.randint(1, 3) == 1:
            barbarian.warCry(2)
        else:
            barbarian.dealDamage(player)
    else:
        barbarian.groan()
    time.sleep(1.5)

def alchemistAction():

    if alchemist.health > 0:
        if random.randint(1, 3) == 1:
            alchemist.debuffPlayer(player, 2)
        else:
            alchemist.dealDamage(player)
    else:
        alchemist.groan()
    time.sleep(1.5)

def main():

    while True:
        
        gameStatus()

        print('\nChoose an action!')
        print('\n1 - Attack')
        print('2 - Heal')
        print('3 - Charge Weapon')
        command = input('\nType in the corresponding number! ')

        if command == '1':
            playerAttack()
        elif command == '2':
            player.gainHealth(20)
        elif command == '3':
            player.gainAttack(4)
        else:
            print("Congratulations! You do nothing.")

        time.sleep(1.5)

        print('')

        goblinAction()
        barbarianAction()
        alchemistAction()

if __name__ == "__main__":
    main()