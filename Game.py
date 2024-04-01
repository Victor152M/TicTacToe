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

    # Start the game loop
    def play_game(self):
        while (True):
            chosen_key = self.current_player.capture_move()
            
            for event in pygame.event.get():

                # Exit the game
                if event.type == pygame.QUIT:
                    pygame.quit()

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

