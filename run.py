import time
import random
from board import create_grid
from board import print_grid
from ship import Ship
from clear import clear_console


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
            how_to_play = input("Type p to play or h for how to play and press Enter:\n").upper()

            #if the user selects how to play

            if how_to_play == "H":
                print("""*** How to Play ***
                1. Please enter your name and press enter.
                2. The game board is a 10 x 10 grid and each square in the grid will be repersented by number and letter(eg. a7, c2). The position of the ships on the player and computers board will be generated automatically.
                3. Enter your coordinates into the console to fire a shot. You will be notified of a hit or miss.
                4. Player and computers selections will appear on their game board to avoid selecting the same coordinates and help narrow down where ships are located.
                5. A winner is decalred when the players or computers fleet is destroyed.\n
                Legend:
                1. '.' = water or empty space
                2. 'O' = part of ship
                3. 'X' = part of ship that was hit with bullet
                4. '#' = water that was shot with bullet, a miss because it hit no ship.\n"""
                )

                # if its p break the while loop and play the game
            elif instruction == "P":
                break
            # raise an error if player doesn't select correct options
            else:
                raise ValueError()
        # if there is an error prompt the user to of choices available
        except (AttributeError, ValueError):
            print(
                    "Please type p to play or h for how to play and press Enter",
            )