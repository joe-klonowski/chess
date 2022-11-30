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

    def apply_move(self, move):
        # TODO implement castling, promotion, en passant
        starting_square = move[0:2]
        piece_type = self.get_piece_on_square(starting_square)
        ending_square = move[3:5]
        self.pieces.update({starting_square: None, ending_square: piece_type})

    def __eq__(self, other):
        return self.pieces == other.pieces
