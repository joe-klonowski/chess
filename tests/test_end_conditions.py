import copy

from unittest import TestCase

from chess.ChessBoard import ChessBoard
from chess.GameState import GameState
from chess.constants import STARTING_GAME_STATE
from chess.end_conditions import is_checkmate, is_stalemate


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

    def test_is_checkmate_in_stalemated_position(self):
        board = ChessBoard()
        board.add_piece("black", "K", "a8")
        board.add_piece("white", "K", "e6")
        board.add_piece("white", "Q", "b6")
        game_state = GameState(board, "black")

        self.assertFalse(is_checkmate(game_state))

    def test_is_stalemate_true(self):
        board = ChessBoard()
        board.add_piece("black", "K", "a8")
        board.add_piece("white", "K", "e6")
        board.add_piece("white", "Q", "b6")
        game_state = GameState(board, "black")

        self.assertTrue(is_stalemate(game_state))

    def test_is_stalemate_false(self):
        self.assertFalse(is_stalemate(STARTING_GAME_STATE))

    def test_is_stalemate_in_checkmate_position(self):
        board = ChessBoard()
        board.add_piece("black", "K", "e8")
        board.add_piece("white", "K", "e6")
        board.add_piece("white", "Q", "e7")
        game_state = GameState(board, "black")

        self.assertFalse(is_stalemate(game_state))
