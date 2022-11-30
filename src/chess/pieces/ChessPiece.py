from chess import ChessSquare


class ChessPiece:
    piece_type: str
    square: ChessSquare

    def __eq__(self, other):
        return self.piece_type == other.piece_type and self.square == other.square


def compare_pieces_by_square(a, b):
    return ChessSquare.compare_squares(a.square, b.square)
