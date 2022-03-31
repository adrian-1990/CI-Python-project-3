import time
import random
from models import board
from utils import clear_console


def menu():
    """
    Opening screen to the game
    """
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
            user_prompt = input("Type p to play or i for instructions and press Enter:\n").upper()

            #if the user selects how to play

            if user_prompt == "I":
                print("""
*** How to Play ***\n
1. Please enter your name and press enter.
2. The game board is a 10 x 10 grid and each square in the grid will be repersented by number and letter(eg. a7, c2). 
3. The position of the ships on the player and computers board will be generated automatically.
4. Enter your coordinates into the console to fire a shot. You will be notified of a hit or miss.
5. Player and computers selections will appear on their game board to avoid selecting the same coordinates and help narrow down where ships are located.
6. A winner is decalred when the players or computers fleet is destroyed.\n
Legend:\n
1. '.' = water or empty space
2. 'O' = part of ship
3. 'X' = part of ship that was hit with bullet
4. '#' = water that was shot with bullet, a miss because it hit no ship.\n"""
                )

                # if its p break the while loop and play the game
            elif user_prompt == "P":
                user_name = input(
                    "Please enter your name:\n"
                ).upper()
                break
            # raise an error if player doesn't select correct options
            else:
                raise ValueError()
        # if there is an error prompt the user to of choices available
        except (AttributeError, ValueError):
            print(
                    "Please type p to play or h for how to play and press Enter",
            )

menu()