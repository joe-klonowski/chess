import copy
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

    def test_apply_move_pawn_two_squares(self):
        starting_board_copy = copy.deepcopy(STARTING_BOARD)
        starting_board_copy.apply_move("e2-e4")

        self.assertIsNone(starting_board_copy.get_piece_on_square("e2"))
        self.assertEqual("P", starting_board_copy.get_piece_on_square("e4"))

    def test_apply_move_knight(self):
        starting_board_copy = copy.deepcopy(STARTING_BOARD)
        starting_board_copy.apply_move("g1-f3")

        self.assertIsNone(starting_board_copy.get_piece_on_square("g1"))
        self.assertEqual("N", starting_board_copy.get_piece_on_square("f3"))
