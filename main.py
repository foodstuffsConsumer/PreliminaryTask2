import time

def main():

    while True:

        print('\nChoose an action!')
        print('\n1 - Attack')
        print('2 - Skill')
        print('3 - Other Skill')
        print('4 - Use Item')
        command = input('\nType in the corresponding number! ')

        if command == '1':
            print("You tried to attack... and MISSED! you tried")
        elif command == '2':
            print("wait hold on i haven't even coded this in yet")
        elif command == '3':
            print("You didn't use Other Skill!")
        elif command == '4':
            print("ITEMS: Fish, fish-shaped medkit, fish-shaped sediment, fish-shaped toilet, fish-shaped fish. You don't like fish so all of these are unusuable, sorry.")
        else:
            print("sorry but im completely illiterate outside of the very narrow selection of commands on your menu")

        time.sleep(2)

if __name__ == "__main__":
    main()