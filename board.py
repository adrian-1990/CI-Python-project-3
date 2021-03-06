import random
import time
import pyfiglet
from utils import clear_console

"""
For creating the code for the game board and logic,
I used the below sites for reference:
Pythondex
URL: https://pythondex.com/python-battleship-game
How to code Battlefield game in Python Youtube video:
https://www.youtube.com/watch?v=tF1WRCrd_HQ
"""

"""
Creates all the boards required for the game
"""
PLAYER_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
"""
Ships length to be accessed in place_ships
Length of ships were taken from the board game
Carrier : 5
Battleship : 4
Destroyer : 3
Submarine : 3
Patrolboat : 2
"""
SHIPS_LENGTHS = [2, 3, 3, 4, 5]

letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}


# creates players game board
def print_board(board):
    print("   A B C D E F G H I J")
    print("   +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        # for row_number less than 10 add spacing, fixed alignment on board
        print("%s%d|%s|" % (" " if row_number < 10 else "", row_number, "|".join(row)))
        row_number += 1


def place_ship(board):
    """
    The place ship function loops throught the lengths of the ships and then
    loops until the ship fits and dosen't overlap any other ships on the board
    and then places the ship.
    """
    #  loop through length of ships
    for ship_length in SHIPS_LENGTHS:
        #  check ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = (
                    random.choice(["H", "V"]),
                    random.randint(0, 9),
                    random.randint(0, 9),
                )
                if fit_ship_check(ship_length, row, column, orientation):
                    #  check if ship overlaps
                    if not ship_overlap(board, row, column, orientation, ship_length):
                        # if no overlap, place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "O"
                        break
            else:
                place_ship = True
                print("Place ship with a length of " + str(ship_length) + "\n")
                row, column, orientation = user_input(place_ship)
                if fit_ship_check(ship_length, row, column, orientation):
                    # check if ship overlaps
                    if ship_overlap(board, row, column, orientation, ship_length):
                        print(
                            "Your ship doesn't fit there, please try a differant location... \n"
                        )
                        time.sleep(2)
                    else:
                        print("Ship placed, lets place your next vessel... \n")
                        time.sleep(2)
                        clear_console()
                        # if no overlap, place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "O"
                        print_board(PLAYER_BOARD)
                        break


def fit_ship_check(SHIP_LENGTH, row, column, orientation):
    """
    The fit_ship_check checks if the ships inputted fit on the board
    """
    if orientation == "H":
        if column + SHIP_LENGTH > 10:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 10:
            return False
        else:
            return True


def ship_overlap(board, row, column, orientation, ship_length):
    """
    The ship_overlap function checks if inputted ships overlap any existing
    ships already on the board
    """
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "O":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "O":
                return True
    return False


def user_input(place_ship):
    """
    user_input function takes the coordinates entered to place the users ships
    User selects if the want to place horizontal / vertical, then row / column
    Computers ships are randomly place onto their board.
    """
    if place_ship == True:
        while True:
            try:
                orientation = input(
                   "Do you want to place the ship Horizontal(H) or Vertical(V): \n"
                ).upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print(
                    "Your ship doesn't fit there, please try a differant location... \n"
                )
        while True:
            try:
                row = input("Enter the row of the ship (1-10): \n")
                if row in "12345678910":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-10\n")
        while True:
            try:
                column = input("Enter the column of the ship (A-J):\n").upper()
                if column not in "ABCDEFGHIJ":
                    print("Please enter a valid letter between A-J\n")
                else:
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-J\n")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row of the ship (1-10): \n")
                if row in "12345678910":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-10\n")
        while True:
            try:
                column = input("Enter the column of the ship (A-J):\n").upper()
                if column not in "ABCDEFGHIJ":
                    print("Please enter a valid letter between A-J\n")
                else:
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-J\n")
        return row, column


def hit_count(board):
    """
    The hit_count function counts the number of hits each board.
    Adds a hit icon "X" everytime a ship is hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    """
    The turn function swaps turns between the user and computer
    Will keep running until players / computers fleet is sunk
    """
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == ".":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "O":
            board[row][column] = "X"
            print("It's a hit, let's keep up the attack!!!!\n")
            time.sleep(2)
        else:
            board[row][column] = "#"
            print("We missed, all we hit was water on that shot!!\n")
            time.sleep(2)
    else:
        row, column = random.randint(0, 9), random.randint(0, 9)
        if board[row][column] == ".":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "O":
            board[row][column] = "X"
            print("Computer taking aim...\n")
            time.sleep(2)
            print("We are hit, the enemy has struck one of our ships!\n")
            time.sleep(2)
        else:
            board[row][column] = "#"
            print("Computer taking aim...\n")
            time.sleep(2)
            print("The enemy has missed, let's continue our assault...\n")
            time.sleep(2)
            clear_console()


def play_game():
    clear_console()
    # Computer places ships automatically
    # COMPUTER_BOARD remains hidden so player cannot see where ships are placed
    place_ship(COMPUTER_BOARD)
    # Players board is displayed
    print_board(PLAYER_BOARD)
    # Place ships on the players board
    place_ship(PLAYER_BOARD)
    clear_console()

    while True:
        # Player turn
        while True:
            clear_console()
            print(pyfiglet.figlet_format("BATTLESHIPS", font="digital"))
            print("PLAYERS BOARD:\n")
            print_board(COMPUTER_GUESS_BOARD)
            print("\nCOMPUTERS BOARD:\n")
            print_board(PLAYER_GUESS_BOARD)
            print("\nEnter a location for us to attack...\n")
            turn(PLAYER_GUESS_BOARD)
            time.sleep(2)
            break
        # total SHIPS_LENGTH = 17, when hit_countr = 17 a winner is declared
        if hit_count(PLAYER_GUESS_BOARD) == 17:
            clear_console()
            print(pyfiglet.figlet_format("YOU WIN!\n", font="slant"))
            print("The enemy's fleet is destroyed and lying on the ocean floor.\n")
            break
        # Computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            clear_console()
            break
        if hit_count(COMPUTER_GUESS_BOARD) == 17:
            clear_console()
            print(pyfiglet.figlet_format("YOU LOSE!\n", font="slant"))
            print(
                "Your fleet has been destroyed, as Captain you must go down with the ship...\n"
            )
            break
