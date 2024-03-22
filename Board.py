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

        # Background color
        self.screen.fill(self.board_color)

        # Drawing the horizontal lines
        pygame.draw.line(self.screen, self.line_color, (0, self.height / 3),
                        (self.width, self.height / 3), width = 1)
        
        pygame.draw.line(self.screen, self.line_color, (0, 2 * self.height / 3),
                        (self.width, 2 * self.height / 3), width = 1)
            

        # Drawing the vertical lines
        pygame.draw.line(self.screen, self.line_color, (self.width / 3, 0),
                        (self.width / 3, self.height), width = 1)
        
        pygame.draw.line(self.screen, self.line_color, (2 * self.width / 3, 0),
                        (2 * self.width / 3, self.height), width = 1)


        pygame.display.update()


    def check_winner(self):
        pass


    def is_board_full(self):
        pass
   

    def draw_X(self):
        pass

    def draw_0(self):
        pass