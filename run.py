import time
import random
from models.board import print_board, board, validate_grid_and_place_ship, place_ships
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
            user_prompt = input("Type p to play or i for instructions and press Enter:\n").upper()

            #if the user selects how to play

            if user_prompt == "I":
                clear_console()
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
                clear_console()
                user_name = input(
                    "Please enter your name:\n"
                ).upper()
                clear_console()
                print("Welcome " + user_name + ", the game is about to begin...\n")
                time.sleep(2)
                print("Players board loading...\n")
                time.sleep(2)
                print("Computers board loading...\n")
                time.sleep(2)
                print("Boards loaded, enjoy the game...\n")
                time.sleep(2)
                break
            # raise an error if player doesn't select correct options
            else:
                raise ValueError()
        # if there is an error prompt the user to of choices available
        except (AttributeError, ValueError):
            print(
                    "Please type p to play or h for how to play and press Enter",
            )

class game:
    welcome_screen()
    clear_console()
    place_ships
    validate_grid_and_place_ship(0, 0, 0, 0)
    print_board(board)

game()