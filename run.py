import time
import random
import pyfiglet
from board import play_game
from utils import clear_console


def welcome_screen():
    """
    Opening screen to the game
    """
    clear_console()
    print(pyfiglet.figlet_format("BATTLESHIPS", font="slant"))

    while True:
        try:
            user_prompt = input(
                "Type p to play or i for instructions and press Enter: \n"
            ).upper()

            # if the user selects how to play

            if user_prompt == "I":
                clear_console()
                print(pyfiglet.figlet_format("HOW TO PLAY!\n", font="slant"))
                print(
                    """
1. Please enter your name and press enter.
2. The game board is a 10 x 10 grid.
3. Each square in the grid will be repersented by number and letter(a7, c2).
4. Each players fleet consists of 5 vessels and based on the board game fleets.
5. The player must position the location of their ships,
   the computers board will be generated automatically.
6. Ships placed VERTICALLY are placed from TOP --> DOWN,
   ships place HORIZONTALLY are placed LEFT --> RIGHT.
7. Enter coordinates into the console to fire a shot,
   You will be notified of a hit or miss.
8. Player and computers selections will appear on their game board,
   to avoid selecting the same coordinates and help narrow down ships position.
9. A winner is decalred when the players or computers fleet is destroyed.\n"""
                )

                print(pyfiglet.figlet_format("LEGEND\n", font="slant"))
                print(
                    """
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
        value = input("Please enter your name:\n").capitalize()

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
    print("You must first place your ships,\n")
    print("make sure to choose well as we don't want your fleet to be sunk...\n")
    time.sleep(2)
    print("Computers board is loaded, hope you enjoy the game...\n")
    time.sleep(2)


class Game:
    welcome_screen()
    clear_console()
    name_input()
    play_game()


Game()

