import os
import time

running = True
tick = 0.5
board_size = 15
wall = "#"

board = [
    [" " for _ in range(board_size)] for _ in range(board_size)
]  # 15*15 board of " "

board[2][2] = "@"  # Random point for vibes


def board_display():
    for i in range(15):
        board[0][i] = wall  # top row
        board[14][i] = wall  # bottom row
        board[i][0] = wall  # left column
        board[i][-1] = wall  # right column

    for row in board:
        print(" ".join(row))


def move_right():
    for i in range(board_size):
        board[4][i] = "@"


def clear_term():
    time.sleep(tick)
    os.system("clear")


if __name__ == "__main__":
    while running:
        move_right()
        board_display()
        clear_term()

# Outcome
"""
####################
#                  #
#     oooo>        #
#                  #
#          *       #
#                  #
####################
"""
# Additions
"""
improve the display function
find a way to clear terminal
move something
food 
classes
done
"""
