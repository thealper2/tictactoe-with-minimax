from constants import ROWS, COLUMNS
from game_logic import check_win, free_space_available, mark_square

def minimax(minimax_board, depth, is_maximizing, board):
    if check_win(2, board):
        return float('inf')
    
    elif check_win(1, board):
        return float('-inf')
    
    elif not free_space_available(board):
        return 0

    if is_maximizing:
        best_score = -10000
        for row in range(ROWS):
            for col in range(COLUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False, board)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        
        return best_score
    else:
        best_score = 10000
        for row in range(ROWS):
            for col in range(COLUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True, board)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        
        return best_score

def best_move(board):
    best_score = -1000
    move = (-1, -1)
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False, board)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move != (-1, -1):
        mark_square(move[0], move[1], 2, board)
        return True
    
    return False
