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
- Handle errors and invalid inputs gracefully

# Determining Specifications

## Functional Specifications

### User Requirements

The user needs to be able to perform various actions, including:
- Using items to assist the user
- Attacking enemies with their weapons

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

Errors in damage and health values calculation are a potential issue.

