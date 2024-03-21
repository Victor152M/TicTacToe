import pygame


class Board:


    def __init__(self, width: int, height: int,rows: int, columns: int
                , board_color: tuple, line_color: tuple):
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        


    def display_board(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))


    def check_winner(sedlf):
        pass


    def is_board_full(self):
        pass
   