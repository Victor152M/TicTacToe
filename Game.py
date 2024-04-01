from Board import Board
from Player import Player
import time
import pygame

class Game:
    def __init__(self, board: Board, players: list):
        self.board = board
        self.players = players
        self.current_player = self.players[0]

    # Initialize the game by creating the board
    def start_game(self):
        self.board.display_board()
        
    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.players[1]:
            self.current_player = self.players[0]

    def make_move(self, key):
        # X or 0 on the first 3 squares (from left to right)
        # 1
        if key == "1" and self.board.map[0][0] == "":
            if self.current_player.marker == "X":
                self.board.map[0][0] = "X"
            else:
                self.board.map[0][0] = "0"

        # 2
        if key == "2" and self.board.map[0][1] == "":
            if self.current_player.marker == "X":
                self.board.map[0][1] = "X"
            else:
                self.board.map[0][1] = "0"

        # 3
        if key == "3" and self.board.map[0][2] == "":
            if self.current_player.marker == "X":
                self.board.map[0][2] = "X"
            else:
                self.board.map[0][2] = "0"


        # X or 0 on the middle squares (from left to right)
        # 4
        if key == "4" and self.board.map[1][0] == "":
            if self.current_player.marker == "X":
                self.board.map[1][0] = "X"
            else:
                self.board.map[1][0] = "0"

        # 5
        if key == "5" and self.board.map[1][1] == "":
            if self.current_player.marker == "X":
                self.board.map[1][1] = "X"
            else:
                self.board.map[1][1] = "0"

        # 6
        if key == "6" and self.board.map[1][2] == "":
            if self.current_player.marker == "X":
                self.board.map[1][2] = "X"
            else:
                self.board.map[1][2] = "0"


        # X or 0 on the last 3 squares (from left to right)
        # 7
        if key == "7" and self.board.map[2][0] == "":
            if self.current_player.marker == "X":
                self.board.map[2][0] = "X"
            else:
                self.board.map[2][0] = "0"

        # 8
        if key == "8" and self.board.map[2][1] == "":
            if self.current_player.marker == "X":
                self.board.map[2][1] = "X"
            else:
                self.board.map[2][1] = "0"

        # 9
        if key == "9" and self.board.map[2][2] == "":
            if self.current_player.marker == "X":
                self.board.map[2][2] = "X"
            else:
                self.board.map[2][2] = "0"


    # Start the game loop
    def play_game(self):
        while (True):
            chosen_key = self.current_player.capture_move()
            
            for event in pygame.event.get():

                # Exit the game
                if event.type == pygame.QUIT:
                    pygame.quit()

            print(event)

            self.make_move(chosen_key)


            if(self.is_game_over()):
                break
            # questionable sleep()
            time.sleep(1)
            self.board.display_board()
            self.switch_player()

    def is_game_over(self) -> bool:
        output = False
        if (self.board.check_winner() != None):
            output = True
        elif (self.board.is_board_full()):
            output = True
        return output; 

