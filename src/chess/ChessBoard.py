from sortedcontainers import SortedDict


class ChessBoard:
    def __init__(self):
        self.pieces = SortedDict({})

    def add_piece(self, piece, square):
        self.pieces.update({square: piece})

    def get_pieces(self):
        return self.pieces

    def get_piece_on_square(self, square):
        return self.pieces.get(square)

    def __eq__(self, other):
        return self.pieces == other.pieces
