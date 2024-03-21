import pygame


class Board:

    def __init__(self):
        
        # Number of rown n columns
        self.rows = 3
        self.columns = 3

        # Style of the game board
        self.board_color = (255, 255, 255)
        self.line_color = (0, 0, 0)

        # Dimension of the board
        self.width = 600
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Window title
        pygame.display.set_caption("TicTacToe Game")

        
    def display_board(self):
        pass


    def check_winner(sedlf):
        pass


    def is_board_full(self):
        pass
   