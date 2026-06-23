class Game:
    def start(self):
        print(f"Chess game started")

class Board:
    def display(self):
        print(f"Chess game displayed")

class Piece:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def move(self):
        print("moving piece")

class King(Piece):
    def __init__(self, color):
        super().__init__("King", color)
    def move(self):
        print("king moves one square")

class Queen(Piece):
    def __init__(self, color):
        super().__init__("Queen", color)
    def move(self):
        print("Queen moves any number of squares")

class Rook(Piece):
    def __init__(self, color):
        super().__init__("Rook", color)
    def move(self):
        print("Rook moves horizontally or vertically")

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("Bishop", color)
    def move(self):
        print("Bishop moves diagonally")

class Knight(Piece):
    def __init__(self, color):
        super().__init__("Knight", color)
    def move(self):
        print("Knight move in L shape")

class Pawn(Piece):
    def __init__(self, color):
        super().__init__("Pawn", color)
    def move(self):
        print("Pawn moves forward one square")

class Player:
    def __init__(self,name):
        self.name=name
    def display_player(self,number):
        print(f"Player {number}: {self.name}")
    def move_piece(self, piece):
        print(f"{self.name} moves {piece.color} {piece.name}")
        piece.move()

game=Game()
game.start()
board=Board()
board.display()
player1=Player("Zainab")
player2=Player("Aiman")
player1.display_player(1)
player2.display_player(2)
print("\n Piece Movements:")
player1.move_piece(King("White"))
player2.move_piece(Queen("Black"))
player1.move_piece(Rook("White"))
player2.move_piece(Bishop("Black"))
player1.move_piece(Knight("White"))
player2.move_piece(Pawn("Black"))