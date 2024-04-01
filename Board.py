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

        # Drawing X or 0 in parallel with the map
        # First square (1)
        if self.map[0][0] == "X":
            self.draw_X(self.width/6, self.height/6)
        elif self.map[0][0] == "0":
            self.draw_0(self.width/6, self.height/6)

        # Second square (2)
        if self.map[0][1] == "X":
            self.draw_X(self.width/2, self.height/6)
        elif self.map[0][1] == "0":
            self.draw_0(self.width/2, self.height/6)

        # 3
        if self.map[0][2] == "X":
            self.draw_X(5 * self.width/6, self.height/6)
        elif self.map[0][2] == "0":
            self.draw_0(5 * self.width/6, self.height/6)

        # 4
        if self.map[1][0] == "X":
            self.draw_X(self.width/6, self.height/2)
        elif self.map[1][0] == "0":
            self.draw_0(self.width/6, self.height/2)

        # 5
        if self.map[1][1] == "X":
            self.draw_X(self.width/2, self.height/2)
        elif self.map[1][1] == "0":
            self.draw_0(self.width/2, self.height/2)

        # 6
        if self.map[1][2] == "X":
            self.draw_X(5 * self.width/6, self.height/2)
        elif self.map[1][2] == "0":
            self.draw_0(5 * self.width/6, self.height/2)

        # 7
        if self.map[2][0] == "X":
            self.draw_X(self.width/6, 5 * self.height/6)
        elif self.map[2][0] == "0":
            self.draw_0(self.width/6, 5 * self.height/6)

        # 8
        if self.map[2][1] == "X":
            self.draw_X(self.width/2, 5 * self.height/6)
        elif self.map[2][1] == "0":
            self.draw_0(self.width/2, 5 * self.height/6)

        # 9
        if self.map[2][2] == "X":
            self.draw_X(5 *self.width/6, 5 * self.height/6)
        elif self.map[2][2] == "0":
            self.draw_0(5 *self.width/6, 5 * self.height/6)

        pygame.display.update()


    def check_winner(self) -> str:
        """
        Returns "None" if there is no winner. 
        Returns "X" if player X is winning. 
        Returns "0" if player 0 is winning.
        """

        board = self.map

        # check rows
        for row in board:
            if row[0] != "" and row.count(row[0]) == len(row):
                return row[0]
            
        # check columns
        for j in range(self.columns):
            if (board[0][j] != "" and board[0][j] == board[1][j] and
                board[0][j] == board[2][j]):
                return board[0][j]
        
        # check diagonals
        if (board[0][0] != "" and board[0][0] == board[1][1] and 
            board[0][0] == board[2][2]):
            return board[0][0]
        if (board[0][2] != "" and board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
            return board[0][2]
                
        return None


    def is_board_full(self) -> bool:
    # Checking if there's any unoccupied space on the map in order to 
    # see if it's full or not
        is_full = True
        for row in self.map:
            if is_full == False:
                break
            for column in row:
                if column == "":
                    is_full = False
                    break
                
        return is_full
   

    def draw_X(self, center_x, center_y) -> None:
        
        # Drawing an X shape
        pygame.draw.line(self.screen, self.line_color, (center_x - 45, center_y - 45), 
                        (center_x + 45, center_y + 45), width=1)
        
        pygame.draw.line(self.screen, self.line_color, (center_x - 45, center_y + 45), 
                        (center_x + 45, center_y - 45), width=1)
        

    def draw_0(self, center_x, center_y) -> None:
        
        # Drawing an 0-like shape (a circle)
        pygame.draw.circle(self.screen, self.line_color, 
                          (center_x, center_y), radius=90, width=1)
        