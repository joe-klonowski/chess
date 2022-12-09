import copy

from chess.ChessBoard import ChessBoard
from unittest import TestCase

from chess.constants import STARTING_BOARD
from constants import KINGS_AND_ONE_PAWN_BOARD


class TestChessBoard(TestCase):
    def test_empty_board(self):
        new_board = ChessBoard()
        self.assertEqual(dict(), new_board.get_pieces())

    def test_add_piece(self):
        queen_on_d1 = dict({"d1": ("white", "Q")})

        new_board = ChessBoard()
        new_board.add_piece("white", "Q", "d1")

        self.assertEqual(queen_on_d1, new_board.get_pieces())

    def test_remove_piece(self):
        new_board = ChessBoard()
        new_board.add_piece("white", "Q", "d1")
        new_board.add_piece("black", "Q", "d8")
        new_board.remove_piece("d8")

        queen_on_d1 = dict({"d1": ("white", "Q")})
        self.assertEqual(queen_on_d1, new_board.get_pieces())

    def test_get_piece_on_square_with_empty_square(self):
        self.assertIsNone(STARTING_BOARD.get_piece_on_square("a3"))

    def test_get_piece_on_square_with_nonempty_square(self):
        result = STARTING_BOARD.get_piece_on_square("a2")
        self.assertEqual(("white", "P"), result)

    def test_apply_move_pawn_two_squares(self):
        starting_board_copy = copy.deepcopy(STARTING_BOARD)
        starting_board_copy.apply_move("e2-e4")

        self.assertIsNone(starting_board_copy.get_piece_on_square("e2"))
        self.assertEqual(("white", "P"), starting_board_copy.get_piece_on_square("e4"))

    def test_apply_move_knight(self):
        starting_board_copy = copy.deepcopy(STARTING_BOARD)
        starting_board_copy.apply_move("g1-f3")

        self.assertIsNone(starting_board_copy.get_piece_on_square("g1"))
        self.assertEqual(("white", "N"), starting_board_copy.get_piece_on_square("f3"))

    def test_get_pieces_for_color_white(self):
        actual = KINGS_AND_ONE_PAWN_BOARD.get_pieces_for_color("white")

        expected = dict({
            "e1": ("white", "K"),
            "e2": ("white", "P"),
        })

        self.assertEqual(expected, actual)
