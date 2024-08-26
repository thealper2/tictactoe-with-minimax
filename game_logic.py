import numpy as np
from constants import ROWS, COLUMNS, BLACK
from drawing import draw_lines

def mark_square(row, col, player, board):
    board[row][col] = player

def available_square(row, col, board):
    return board[row][col] == 0

def free_space_available(board):
    return np.any(board == 0)

def check_win(player, board):
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        
    for col in range(COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def restart_game(screen, board):
    screen.fill(BLACK)
    draw_lines(screen)
    for row in range(ROWS):
        for col in range(COLUMNS):
            board[row][col] = 0