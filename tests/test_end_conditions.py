import copy

from unittest import TestCase

from chess.ChessBoard import ChessBoard
from chess.GameState import GameState
from chess.constants import STARTING_GAME_STATE
from chess.end_conditions import is_checkmate


class TestEndConditions(TestCase):
    def test_is_checkmate_true(self):
        board = ChessBoard()
        board.add_piece("black", "K", "e8")
        board.add_piece("white", "K", "e6")
        board.add_piece("white", "Q", "e7")
        game_state = GameState(board, "black")

        self.assertTrue(is_checkmate(game_state))

    def test_is_checkmate_false(self):
        self.assertFalse(is_checkmate(STARTING_GAME_STATE))
