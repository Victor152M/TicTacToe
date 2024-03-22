from Board import Board

class Player():
    def __init__(self, name: str, marker: str) -> int:
        self.name = name
        self.marker = marker
    
    def capture_move(self):
        print(f"{self.name}'s turn")
        # Input from the keyboar for the move to make
        Board.draw_X()