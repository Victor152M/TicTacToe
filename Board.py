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

        self.map = [
            ["","",""],
            ["","",""],
            ["","",""]
        ]

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


    def check_winner(self, players = ["Player_1", "Player_2"]) -> str:
        """
        Returns None if there is no winner
        Returns the name of the winning player otherwise
        
        Keyword arguments: 
        players -- list with player names (first entry is for "X", second entry is for "0")
        """
        winner = None
        number_of_matching_elements_row = 0
        
        #For now it only verifies the rows
        for i in range(self.rows):
            row_first_element = self.map[i][0]
            number_of_matching_elements_row = 0
            number_of_matching_elements_column = 0
            for j in range(self.columns):
                if (self.map[i][j] == row_first_element):
                    number_of_matching_elements_row += 1
                    if number_of_matching_elements_row == self.rows:
                        if self.map[i][j] == "X":
                            winner = players[0]
                        else:
                            winner = players[1]
                
        return winner


    def is_board_full(self):
    
    # Checking if there's any unoccupied space on the map in order to 
    # see if it's full or not
        full = True
        for row in self.map:
            if full == False:
                break
            for column in row:
                if column == "":
                    full = False
                    break
   

    def draw_X(self) -> None:
        
        # Drawing an x shape
        pygame.draw.line(self.screen, self.line_color, (center_x - 45, center_y - 45), 
                        (center_x + 45, center_y + 45), width=1)
        
        pygame.draw.line(self.screen, self.line_color, (center_x - 45, center_y + 45), 
                        (center_x + 45, center_y - 45))
        

    def draw_0(self) -> None:
        
        # Drawing an 0-like shape (a circle)
        pygame.draw.circle(self.screen, self.line_color, (center_x, center_y), radius=90, width=1)
        