import random
import time
from .ship import Ship
from utils import clear_console, validate_coordinates

PLAYER_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_GUESS_BOARD = [[" "] * 10 for i in range(10)]

SHIPS_LENGTHS = [2, 3, 3, 4, 5]

class GameBoard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
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
        return letters_to_numbers
    # creates the players game board
    def print_board(self):
        print("  A B C D E F G H I J")
        print("  +-+-+-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

"""
New code
"""

def place_ship(board):
    """
    The place ship function loops throught the lengths of the ships and then
    loops until the ship fits and dosent overlap any other ships on the board
    and then places the ship.
    """
    #  loop through length of ships
    for ship_length in SHIPS_LENGTHS:
        #  loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 9), random.randint(0, 9)
                if fit_ship_check(ship_length, row, column, orientation):
                    #  check if ship overlaps
                    if not ship_overlap(board, row, column, orientation,
                                        ship_length):
                        #  place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "O"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if fit_ship_check(ship_length, row, column, orientation):
                    # check if ship overlaps
                    if ship_overlap(board, row, column, orientation,
                                    ship_length):
                        print(PHASE)
                        print("THE SHIP DOSENT FIT HERE \n")
                    else:
                        print(PHASE)
                        print("EXCELLENT POSITIONING OF THE SHIP \n")
                        # place ship
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
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
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
    The user_input function takes input from the user to enter where they want
    to place their ships as well as guessing the computers ships on the board
    """
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): \n").upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid orientaion (H or V)")
        while True:
            try:
                row = input("Enter the row of the ship 0-9: \n")
                if row in '0123456789':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 0-9")
        while True:
            try:
                column = input("Enter the column of the ship A-J: \n").upper()
                if column not in 'ABCDEFGHIJ':
                    print("Please enter a valid letter between A-J")
                else:
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-J")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row of the ship 0-9: \n")
                if row in '0123456789':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 0-9")
        while True:
            try:
                column = input("Enter the column of the ship A-J: \n").upper()
                if column not in 'ABCDEFGH':
                    print("Please enter a valid letter between A-J")
                else:
                    column = letters_conversion[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-J")
        return row, column


def hit_count(board):
    """
    The hit_count function counts the number of hits each board (Player,
    Computer) has taken
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    """
    The turn function goes through the users and computers turns
    """
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == ".":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "O":
            board[row][column] = "X"
            print("WE HIT THEM, GREAT SHOT CAPTAIN")
        else:
            board[row][column] = "#"
            print("WE MISSED, WE WILL GET THEM ON THE NEXT SHOT")
    else:
        row, column = random.randint(0, 9), random.randint(0, 9)
        if board[row][column] == ".":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "O":
            board[row][column] = "X"
            print("WE ARE HIT, FIRE BACK!")
            print("COMPUTERS BOARD \n")
        else:
            board[row][column] = "-"
            print("THE COMPUTER MISSED, PHEW...\n")
            print("COMPUTERS BOARD \n")

def play_game():
    # Computer places ships
    place_ship(COMPUTER_BOARD)
    # Computer board displayed
    # print_board(COMPUTER_BOARD)
    # Player board displayed
    GameBoard(PLAYER_BOARD)
    # Player places ships
    place_ship(PLAYER_BOARD)

    while True:
        # Player turn
        while True:
            print(PHASE)
            print('GUESS A BATTLESHIP LOCATION CAPTAIN!\n')
            print_board(PLAYER_GUESS_BOARD)
            turn(PLAYER_GUESS_BOARD)
            time.sleep(2)
            break
        if hit_count(PLAYER_GUESS_BOARD) == 17:
            print("\u001b[32mYOU WON!\u001b[0m, BRILLIANT SHOOTING CAPTAIN")
            break
        # Computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            time.sleep(1)
            break
        print_board(COMPUTER_GUESS_BOARD)
        if hit_count(COMPUTER_GUESS_BOARD) == 17:
            print(
                "UNLUCKY \u001b[31mYOU LOSE\u001b[0m CAPTAIN, WE WILL GET THEM \
                NEXT TIME")
            break

"""
Old code
"""

"""
class build_board:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in "0123456789":
                print("Not an appropriate choice, please select a valid row")
                x_row = input("Enter the row of the ship: ")
            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGHIJ":
                print("Not an appropriate choice, please select a valid column")
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input, please try again")
            return self.get_user_input()

    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
                return hit_ships

def RunGame():
    computer_board = GameBoard([[" "] * 10 for i in range(10)])
    user_guess_board = GameBoard([[" "] * 10 for i in range(10)])
    build_board.create_ships(computer_board)
    bullets = 50
    while bullets > 0:
      GameBoard.print_board(user_guess_board)
      # get user import
      user_x_row, user_y_column = build_board.get_user_input(object)
      # check if guesses duplicated
      while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "-":
          print("You guessed that already, try again")
          user_x_row, user_y_column = build_board.get_user_input(object)
      # check for hit or miss
    if computer_board.board[user_x_row][user_y_column] == "X":
        print("You sunk 1 of my battleship!")
        user_guess_board.board[user_x_row][user_y_column] = "X"
    else:
          print("You missed")
          user_guess_board.board[user_x_row][user_y_column] = "-"
      # Check if you won or lost the game
    if build_board.count_hit_ships(user_guess_board) == 5:
        print("You have sunk all my battleships")
        break
    else:
        bullets -= 1
        print(f"You have {bullets} remaining")
        if bullets == 0:
            print("You are all out of bullets")
            GameBoard.print_board(user_guess_board)
            break
"""