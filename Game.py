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
        

        # X or 0 on the first 3 squares (from left to right)
        # 1
        if key == "1" and possible_keys.get("1") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/6, self.board.height/6)

                # Trebuie self.possible_keys aici? :()
                possible_keys["1"] = "X"
            else:
                self.board.draw_0(self.board.width/6, self.board.height/6)

                # Trebuie self.possible_keys aici? :()
                possible_keys["1"] = "0"

        # 2
        if key == "2" and possible_keys.get("2") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/2, self.board.height/6)
                possible_keys["2"] = "X"
            else:
                self.board.draw_0(self.board.width/2, self.board.height/6)
                possible_keys["2"] = "0"

        # 3
        if key == "3" and possible_keys.get("3") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(5 * self.board.width/6, self.board.height/6)
                possible_keys["3"] = "X"
            else:
                self.board.draw_0(5 * self.board.width/6, self.board.height/6)
                possible_keys["3"] = "0"


        # X or 0 on the middle squares (from left to right)
        # 4
        if key == "4" and possible_keys.get("4") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/6, self.board.height/2)
                possible_keys["4"] = "X"
            else:
                self.board.draw_0(self.board.width/6, self.board.height/2)
                possible_keys["4"] = "0"

        # 5
        if key == "5" and possible_keys.get("5") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/2, self.board.height/2)
                possible_keys["5"] = "X"
            else:
                self.board.draw_0(self.board.width/2, self.board.height/2)
                possible_keys["5"] = "0"

        # 6
        if key == "6" and possible_keys.get("6") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(5 * self.board.width/6, self.board.height/2)
                possible_keys["6"] = "X"
            else:
                self.board.draw_0(5 * self.board.width/6, self.board.height/2)
                possible_keys["6"] = "0"


        # X or 0 on the last 3 squares (from left to right)
        # 7
        if key == "7" and possible_keys.get("7") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/6, 5 * self.board.height/6)
                possible_keys["7"] = "X"
            else:
                self.board.draw_0(self.board.width/6, 5 * self.board.height/6)
                possible_keys["7"] = "0"

        # 8
        if key == "8" and possible_keys.get("8") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(self.board.width/2, 5 * self.board.height/6)
                possible_keys["8"] = "X"
            else:
                self.board.draw_0(self.board.width/2, 5 * self.board.height/6)
                possible_keys["8"] = "0"

        # 9
        if key == "9" and possible_keys.get("9") == "":
            if self.current_player.marker == "X":
                self.board.draw_X(5 *self.board.width/6, 5 * self.board.height/6)
                possible_keys["9"] = "X"
            else:
                self.board.draw_0(5 * self.board.width/6, 5 * self.board.height/6)
                possible_keys["9"] = "0"


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

