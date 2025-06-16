# **11SE TASK 2 2025 - TURN-BASED COMBAT GAME**

# Requirements Definition

## Functional Requirements

The program is a text-based turn-based combat game. Its capabilities must include:
- Having enemies which attack the player
- Allowing the player to use moves to combat said enemies

## Non-Functional Requirements

The program should:
- Run quickly and smoothly
- Be easy to use
- Lack errors

# Determining Specifications

## Functional Specifications

### User Requirements

The user needs to be able to perform various actions, including:
- Attacking enemies with their weapons
- Blocking enemy attacks

### Input & Output

The user's inputs will consist of a number typed in. Certain numbers will correspond to a command, which changes depending on context.
Output from the program should consist of information regarding the state of the game, such as the status of the player or enemy, as well as a list of commands which can be performed.

### Core Features

At its core, the program must be able to:
- Display the state of the game, including enemy and player health
- Allow the player to perform various actions, including attacking and using items
- Feature enemies which also perform various actions, including but not limited to self-buffs and attacks

### User Interaction

Users will interact with the program through a command line and text input. 

## Non-Functional Specifications

### Performance

Each task performed by the system should take under a second.

### Reliability

Errors in calculations of damage and health values are a potential issue.

# Sprint 1

## Build

```
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
```

## Review
This build acted as a framework for the program - and it did its job accordingly.

# Sprint 2

## Build

## Review

# Sprint 3

## Build

## Review