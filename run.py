import time
import random
from board import play_game
from utils import clear_console


def welcome_screen():
    """
    Opening screen to the game
    """
    clear_console()
    print(
        """
 ____    _  _____ _____ _     _____ ____  _   _ ___ ____  ____  
| __ )  / \|_   _|_   _| |   | ____/ ___|| | | |_ _|  _ \/ ___| 
|  _ \ / _ \ | |   | | | |   |  _| \___ \| |_| || || |_) \___ \ 
| |_) / ___ \| |   | | | |___| |___ ___) |  _  || ||  __/ ___) |
|____/_/   \_\_|   |_| |_____|_____|____/|_| |_|___|_|   |____/ 
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
 _   _                 _          ____  _             
| | | | _____      __ | |_ ___   |  _ \| | __ _ _   _ 
| |_| |/ _ \ \ /\ / / | __/ _ \  | |_) | |/ _` | | | |
|  _  | (_) \ V  V /  | || (_) | |  __/| | (_| | |_| |
|_| |_|\___/ \_/\_/    \__\___/  |_|   |_|\__,_|\__, |
                                                |___/                                                                                   
\n
1. Please enter your name and press enter.
2. The game board is a 10 x 10 grid, each square in the grid will be repersented by number and letter(a7, c2). 
3. Each players fleet consists of 5 vessels. These length of the ships are based on the Battleship board game.
4. The player must position the location of their ships, the computers board will be generated automatically.
5. Ships placed VERTICALLY are placed from TOP --> DOWN, ships place HORIZONTALLY are placed LEFT --> RIGHT.
6. Enter your coordinates into the console to fire a shot. You will be notified of a hit or miss.
7. Player and computers selections will appear on their game board to avoid selecting the same coordinates and help narrow down where ships are located.
8. A winner is decalred when the players or computers fleet is destroyed.\n
 _                              _ 
| |    ___  __ _  ___ _ __   __| |
| |   / _ \/ _` |/ _ \ '_ \ / _` |
| |__|  __/ (_| |  __/ | | | (_| |
|_____\___|\__, |\___|_| |_|\__,_|
        |___/                                                                
\n
1. '.' = water or empty space
2. 'O' = part of ship
3. 'X' = part of ship that was hit with bullet
4. '#' = water that was shot with bullet, a miss because it hit no ship.\n"""
                )

                # if its p break the while loop and play the game
            elif user_prompt == "P":
                clear_console()
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
    user_name = ""
    while not user_name:
        value = input("Please enter your name:\n")

        if value == "computer":
            print("That is my name human!!! Please enter your own name... \n")
        elif len(value) == 0:
            print("I appreciate the secrecy but I must know your name...\n")
        else:
            user_name = value
    print("Welcome " + user_name + ", the game is about to begin...\n")
    time.sleep(2)
    print("This is based on the classic Battlefield board game...\n")
    time.sleep(2)
    print(
        "You must first place your ships, make sure to choose well as we don't want your fleet to be sunk...\n"
    )
    time.sleep(2)
    print("Computers board is loaded, hope you enjoy the game...\n")
    time.sleep(2)


class Game:
    welcome_screen()
    clear_console()
    name_input()
    clear_console()
    play_game()


Game()
