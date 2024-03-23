from Board import Board

class Player():
    def __init__(self, name: str, marker: str) -> int:
        self.name = name
        self.marker = marker
    
    def capture_move(self) -> int:
        print(f"{self.name}'s turn")
        possible_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        move = 0
        while move not in possible_moves:
            move = input("Enter a number from 1 to 9: ")
        return move
        

        
