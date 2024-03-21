from Board import Board
from Player import Player

class Game:
    def __init__(self, board: Board, players: list):
        self.board = board
        self.players
        self.current_player = self.players[0]

    # Initialize the game by creating the board
    def start_game(self):
        self.board.display_board()
        
    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.player[1]:
            self.current_player = self.player[0]

    # Start the game loop
    def play_game(self):
        while (True):
            self.current_player.choose_move()
            if(is_game_over() or is_board_full):
                break
            self.board.display_board()
            switch_player()

    def is_game_over(self) -> bool:
        self.board.check_winner()
        #do something about is_board_full()
        self.board.is_board_full()

