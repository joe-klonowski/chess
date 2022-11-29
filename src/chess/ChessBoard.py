from functools import cmp_to_key

from ChessPiece import ChessPiece, compare_pieces_by_square
from ChessSquare import from_string


class ChessBoard:
    def __init__(self):
        self.pieces_sorted = False
        self.pieces = []

    def add_piece(self, piece, square):
        """
        :param piece:
        :param square: Can be a ChessSquare or a str like "b8"
        :return:
        """
        if isinstance(square, str):
            square = from_string(square)
        self.pieces_sorted = False
        self.pieces.append(ChessPiece(piece, square))

    def get_pieces(self):
        self.__sort_pieces_if_necessary()
        return self.pieces

    def __sort_pieces_if_necessary(self):
        if not self.pieces_sorted:
            self.pieces = sorted(self.pieces, key=cmp_to_key(compare_pieces_by_square))
            self.pieces_sorted = True

    def __eq__(self, other):
        self.__sort_pieces_if_necessary()
        other.__sort_pieces_if_necessary()
        return self.pieces == other.pieces
