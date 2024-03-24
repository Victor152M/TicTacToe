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
        possible_keys = {
                        "1": self.board.map[0][0], "2": self.board.map[0][1], 
                        "3": self.board.map[0][2], "4": self.board.map[1][0], 
                        "5": self.board.map[1][1], "6": self.board.map[1][2], 
                        "7": self.board.map[2][0], "8": self.board.map[2][1], 
                        "9": self.board.map[2][2]
                        }
        
        # If the input is 1 then an X or 0 will be drawn in the first square
        if key == "1" and possible_keys.get("1") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/6, self.board.height/6)
            else:
                self.board.draw_0(self.board.width/6, self.board.height/6)


        # If the input is 2 then an X or 0 will be drawn in the second square
        if key == "1" and possible_keys.get("1") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/3, self.board.height/6)
            else:
                self.board.draw_0(self.board.width/3, self.board.height/6)

        
        # If the input is 3 then an X or 0 will be drawn in the third square and so on
        if key == "1" and possible_keys.get("1") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(5*self.board.width/6, self.board.height/6)
            else:
                self.board.draw_0(5*self.board.width/6, self.board.height/6)


    # Start the game loop
    def play_game(self):
        while (True):
            chosen_key = self.current_player.capture_move()
            
            for event in pygame.event.get():

                # Exit the game
                if event.type == pygame.QUIT:
                    break

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

