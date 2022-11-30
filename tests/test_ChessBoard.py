from sortedcontainers import SortedDict

from chess.ChessBoard import ChessBoard
from unittest import TestCase

from chess.constants import STARTING_BOARD


class TestChessBoard(TestCase):
    def test_empty_board(self):
        new_board = ChessBoard()
        self.assertEqual(SortedDict({}), new_board.get_pieces())

    def test_add_piece(self):
        queen_on_d1 = SortedDict({"d1": "Q"})

        new_board = ChessBoard()
        new_board.add_piece("Q", "d1")

        self.assertEqual(queen_on_d1, new_board.get_pieces())

    def test_get_piece_on_square_with_empty_square(self):
        self.assertIsNone(STARTING_BOARD.get_piece_on_square("a3"))

    def test_get_piece_on_square_with_nonempty_square(self):
        result = STARTING_BOARD.get_piece_on_square("a2")
        self.assertEqual("P", result)
