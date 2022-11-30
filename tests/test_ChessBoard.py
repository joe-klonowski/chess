from sortedcontainers import SortedDict

from chess.ChessBoard import ChessBoard
from chess.ChessPiece import ChessPiece
from chess.ChessSquare import from_string
from unittest import TestCase


class TestChessBoard(TestCase):
    def test_empty_board(self):
        new_board = ChessBoard()
        self.assertEqual(SortedDict({}), new_board.get_pieces())

    def test_add_piece(self):
        queen_on_d1 = SortedDict({"d1": "Q"})

        new_board = ChessBoard()
        new_board.add_piece("Q", "d1")

        self.assertEqual(queen_on_d1, new_board.get_pieces())
