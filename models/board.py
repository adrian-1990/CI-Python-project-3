import random
import time
from .ship import Ship, Carrier, Battleship, Destroyer, Submarine, PatrolBoat
from utils import clear_console, validate_coordinates


class GameBoard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        return {
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

    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class build_board:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 10), random.randint(0, 10)
            while self.board[self.x_row][self.y_column] == "O":
                self.x_row, self.y_column = random.randint(0, 10), random.randint(0, 10)
            self.board[self.x_row][self.y_column] = "O"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in "12345678910":
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


