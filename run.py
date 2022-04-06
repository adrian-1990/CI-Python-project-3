import time
import random
from models.board import play_game
from utils import clear_console


def welcome_screen():
    """
    Opening screen to the game
    """
    clear_console()
    print(
        """
 ______                 _            _     _            
(____  \       _   _   | |          | |   (_)           
 ____)  ) ____| |_| |_ | | ____  ___| | _  _ ____   ___ 
|  __  ( / _  |  _)  _)| |/ _  )/___) || \| |  _ \ /___)
| |__)  | ( | | |_| |__| ( (/ /|___ | | | | | | | |___ |
|______/ \_||_|\___)___)_|\____|___/|_| |_|_| ||_/(___/ 
                                            |_| 
        
\n
"""
    )

    while True:
        try:
            user_prompt = input(
                "Type p to play or i for instructions and press Enter: \n"
            ).upper()

            # if the user selects how to play

            if user_prompt == "I":
                clear_console()
                print(
                    """
*** How to Play ***\n
1. Please enter your name and press enter.
2. The game board is a 10 x 10 grid and each square in the grid will be repersented by number and letter(eg. a7, c2). 
3. Each players fleet consists of 5 vessels. These length of the ships are based on the Battleship board game.
4. The player must position the location of their ships, the computers board will be generated automatically.
5. Enter your coordinates into the console to fire a shot. You will be notified of a hit or miss.
6. Player and computers selections will appear on their game board to avoid selecting the same coordinates and help narrow down where ships are located.
7. A winner is decalred when the players or computers fleet is destroyed.\n
Legend:\n
1. '.' = water or empty space
2. 'O' = part of ship
3. 'X' = part of ship that was hit with bullet
4. '#' = water that was shot with bullet, a miss because it hit no ship.\n"""
                )

                # if its p break the while loop and play the game
            elif user_prompt == "P":
                break
            # raise an error if player doesn't select correct options
            else:
                raise ValueError()
        # if there is an error prompt the user to of choices available
        except (AttributeError, ValueError):
            print(
                "Please type p to play or h for how to play and press Enter",
            )


def name_input():
    clear_console()
    user_name = input("Please enter your name:\n").upper()
    if user_name.lower() == "computer":
        print("That is my name human!!! Please enter your own name: \n")
        user_name = input("Please enter your name:\n").upper()
    elif len(user_name) == 0:
        print("I appreciate the secrecy but I must know your name...")
        user_name = input("Please enter your name:\n").upper()
    print("Welcome " + user_name + ", the game is about to begin...\n")
    time.sleep(2)
    print("This is based on the classic Battlefield board game\n")
    time.sleep(2)
    print(
        "You must first place your ships, make sure to choose well as we don't want your fleet to be sunk...\n"
    )
    time.sleep(2)
    print("Computers board is loaded, hope you enjoy the game...\n")
    time.sleep(2)


class Game:
    welcome_screen()
    name_input()
    play_game()


Game()