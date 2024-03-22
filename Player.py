from Board import Board

class Player():
    def __init__(self, name: str, marker: str) -> int:
        self.name = name
        self.marker = marker
    
    def capture_move(self):
        print(f"{self.name}'s turn")
        move = input("Enter a number from 1 to 9: ")
        

        
