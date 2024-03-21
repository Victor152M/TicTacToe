if __name__ == "__main__":
    board = Board()

    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "0")
    players = [player1, player2]

    game = Game(board, player, players)
    game.start_game()
    game.play_game()