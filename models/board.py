import random
from utils import clear_console

"""
The code for creating the players board was used after
finding a solution on the web
Credit: https://bigmonty12.github.io/battleship
"""


def build_board(dims):
    return [['.' for count in range(dims)] for count in range(dims)]

def print_board(board):
    for b in board:
        print(*b)

board = build_board(10)
print_board(board)