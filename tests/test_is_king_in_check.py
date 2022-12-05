import copy
from sortedcontainers import SortedDict

from chess.ChessBoard import ChessBoard
from unittest import TestCase

from chess.constants import STARTING_BOARD
from chess.is_king_in_check import is_king_in_check
from constants import KINGS_AND_ONE_PAWN_BOARD, KINGS_AND_ONE_PAWN_CHECK_GAME_STATE, KINGS_AND_ONE_PAWN_GAME_STATE


class TestIsKingInCheck(TestCase):
    def test_pawn_check(self):
        actual = is_king_in_check(KINGS_AND_ONE_PAWN_CHECK_GAME_STATE)
        self.assertTrue(actual)

    def test_no_check(self):
        actual = is_king_in_check(KINGS_AND_ONE_PAWN_GAME_STATE)
        self.assertFalse(actual)
