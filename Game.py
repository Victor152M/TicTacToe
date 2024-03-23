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
        possible_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        if key == "1" and self.board.map:
            pass


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
        if (self.board.check_winner(self.players) != None):
            output = True
        elif (self.board.is_board_full()):
            output = True
        return output; 

