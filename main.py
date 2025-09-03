import os
import time

# global var
running = True
tick = 0.5
board_size = 15
wall = "#"
head = "@"

board = [
    [" " for _ in range(board_size)] for _ in range(board_size)
]  # 15*15 board of " "

snake = [[3, 2], [4, 2], [5, 2]]


def board_display():
    for i in range(15):
        board[0][i] = wall  # top row
        board[14][i] = wall  # bottom row
        board[i][0] = wall  # left column
        board[i][-1] = wall  # right column

    for row in board:
        print(" ".join(row))


def move_snake_right():
    head_x = snake[-1][0] + 1  # increasing x by 1
    head_y = snake[-1][1]  # y stays the sname

    new_head = [head_x, head_y]

    snake.append(new_head)

    snake.pop(0)


def draw_snake():
    for segment in snake:
        x, y = segment
        board[y][x] = "@"


def clear_term():
    time.sleep(tick)
    os.system("clear")

    for row in range(1, board_size - 1):
        for col in range(1, board_size - 1):
            board[row][col] = " "


if __name__ == "__main__":
    while running:
        move_snake_right()
        draw_snake()
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



Snake state:

Draw snake:

Clear board (except walls).

Place "@" at each snake coordinate.

Print the board.

Move snake (right first):

Take head, add +1 to x-coordinate → new head.

Append new head to snake list.

Remove first element (tail).

Loop:

Repeat: clear board → redraw walls → place snake → print → sleep/clear.

Next:

Once this works, add input, food, growth, collisions later.
"""
