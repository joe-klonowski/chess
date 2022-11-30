from functools import cmp_to_key
from sortedcontainers import SortedDict

from chess.ChessPiece import ChessPiece, compare_pieces_by_square
from chess.ChessSquare import from_string, ChessSquare


class ChessBoard:
    def __init__(self):
        self.pieces = SortedDict({})

    def add_piece(self, piece, square):
        """
        :param piece:
        :param square: Can be a ChessSquare or a str like "b8"
        :return:
        """
        square_str = square
        if isinstance(square, ChessSquare):
            square_str = str(square)
        self.pieces.update({square_str: piece})

    def get_pieces(self):
        return self.pieces

    def get_piece_on_square(self, square):
        return self.pieces.get(square)

    def __eq__(self, other):
        return self.pieces == other.pieces
