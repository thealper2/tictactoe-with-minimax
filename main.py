import sys
import pygame
import numpy as np
from constants import WIDTH, HEIGHT, SQUARE_SIZE, GREEN, RED, GRAY, ROWS, COLUMNS
from game_logic import available_square, mark_square, check_win, free_space_available, restart_game
from drawing import draw_lines, draw_figures
from ai import best_move

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe with Minimax Algorithm")

board = np.zeros((ROWS, COLUMNS))

def play_game():
    draw_lines(screen)
    player = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE

                if available_square(mouseY, mouseX, board):
                    mark_square(mouseY, mouseX, player, board)
                    if check_win(player, board):
                        game_over = True
                    player = player % 2 + 1

                if not game_over and player == 2:
                    if best_move(board):
                        if check_win(2, board):
                            game_over = True
                        player = player % 2 + 1

                if not game_over and not free_space_available(board):
                    game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game(screen, board)
                    game_over = False
                    player = 1

        if not game_over:
            draw_figures(screen, board)
        else:
            if check_win(1, board):
                draw_figures(screen, board, GREEN)
                draw_lines(screen, GREEN)
            elif check_win(2, board):
                draw_figures(screen, board, RED)
                draw_lines(screen, RED)
            else:
                draw_figures(screen, board, GRAY)
                draw_lines(screen, GRAY)

        pygame.display.update()

if __name__ == "__main__":
    play_game()
