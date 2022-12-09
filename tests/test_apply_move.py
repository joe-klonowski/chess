import copy

from unittest import TestCase

from chess.apply_move import apply_move
from chess.constants import STARTING_GAME_STATE


class TestApplyMove(TestCase):
    def test_1e4(self):
        actual = apply_move(STARTING_GAME_STATE, "e2-e4")

        expected = copy.deepcopy(STARTING_GAME_STATE)
        expected.board.remove_piece("e2")
        expected.board.add_piece("white", "P", "e4")
        expected.player_to_move = "black"

        self.assertEqual(expected, actual)

    def test_bongcloud(self):
        actual = apply_move(STARTING_GAME_STATE, "e2-e4")
        actual = apply_move(actual, "e7-e5")
        actual = apply_move(actual, "e1-e2")

        expected = copy.deepcopy(STARTING_GAME_STATE)
        expected.board.remove_piece("e2")
        expected.board.remove_piece("e7")
        expected.board.remove_piece("e1")
        expected.board.add_piece("white", "P", "e4")
        expected.board.add_piece("black", "P", "e5")
        expected.board.add_piece("white", "K", "e2")
        expected.player_to_move = "black"

        self.assertEqual(expected, actual)
