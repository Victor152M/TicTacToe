from Game import Game
from Board import Board
from Player import Player

if __name__ == "__main__":
    board = Board()

    playerX = Player("Player 1", "X")
    player0 = Player("Player 2", "0")
    players = [playerX, player0]

    game = Game(board, players)
    game.start_game()
    game.play_game()