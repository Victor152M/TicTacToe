class Player():
    def __init__(self, name: str, marker: str) -> int:
        self.name = name
        self.marker = marker
    
    def choose_move(self):
        print(f"{self.name}'s turn")
