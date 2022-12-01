import copy
from unittest import TestCase

from chess.get_possible_moves import get_possible_moves, get_possible_moves_for_piece, get_possible_moves_for_king, \
    get_relative_square, get_possible_moves_for_pawn
from constants import KINGS_AND_ONE_PAWN_GAME_STATE, KINGS_AND_ONE_BLACK_PAWN_GAME_STATE, KINGS_AND_ONE_ROOK_GAME_STATE


class TestGetPossibleMoves(TestCase):
    def test_get_relative_square_north_one(self):
        actual = get_relative_square("e4", "N", 1)
        expected = "e5"
        self.assertEqual(expected, actual)

    def test_get_relative_square_north_four(self):
        actual = get_relative_square("e4", "N", 4)
        expected = "e8"
        self.assertEqual(expected, actual)

    def test_get_relative_square_north_off_board(self):
        self.assertIsNone(get_relative_square("e4", "N", 5))

    def test_get_relative_square_south_one(self):
        actual = get_relative_square("e4", "S", 1)
        expected = "e3"
        self.assertEqual(expected, actual)

    def test_get_relative_square_south_two(self):
        actual = get_relative_square("e4", "S", 2)
        expected = "e2"
        self.assertEqual(expected, actual)

    def test_get_relative_square_south_off_board(self):
        self.assertIsNone(get_relative_square("e4", "S", 5))

    def test_get_relative_square_east_one(self):
        actual = get_relative_square("e4", "E", 1)
        expected = "f4"
        self.assertEqual(expected, actual)

    def test_get_relative_square_east_two(self):
        actual = get_relative_square("e4", "E", 2)
        expected = "g4"
        self.assertEqual(expected, actual)

    def test_get_relative_square_east_off_board(self):
        self.assertIsNone(get_relative_square("e4", "E", 5))

    def test_get_relative_square_west_one(self):
        actual = get_relative_square("e4", "W", 1)
        expected = "d4"
        self.assertEqual(expected, actual)

    def test_get_relative_square_west_two(self):
        actual = get_relative_square("e4", "W", 2)
        expected = "c4"
        self.assertEqual(expected, actual)

    def test_get_relative_square_west_off_board(self):
        self.assertIsNone(get_relative_square("e4", "W", 5))

    def test_get_relative_square_northeast_one(self):
        actual = get_relative_square("e4", "NE", 1)
        expected = "f5"
        self.assertEqual(expected, actual)

    def test_get_relative_square_northeast_two(self):
        actual = get_relative_square("e4", "NE", 2)
        expected = "g6"
        self.assertEqual(expected, actual)

    def test_get_relative_square_northeast_off_board(self):
        self.assertIsNone(get_relative_square("e4", "NE", 5))

    def test_get_relative_square_northwest_one(self):
        actual = get_relative_square("e4", "NW", 1)
        expected = "d5"
        self.assertEqual(expected, actual)

    def test_get_relative_square_souteast_one(self):
        actual = get_relative_square("e4", "SE", 1)
        expected = "f3"
        self.assertEqual(expected, actual)

    def test_get_relative_square_southwest_one(self):
        actual = get_relative_square("e4", "SW", 1)
        expected = "d3"
        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_king(self):
        actual = get_possible_moves_for_king(KINGS_AND_ONE_PAWN_GAME_STATE, "e1")

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
        }

        self.assertEqual(expected, actual)

    # TODO add test to verify that king can't move into check

    def test_get_possible_moves_for_pawn_starting_square(self):
        actual = get_possible_moves_for_pawn(KINGS_AND_ONE_PAWN_GAME_STATE, "e2")

        expected = {
            "e2-e3",
            "e2-e4"
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_not_starting_square(self):
        new_game_state = copy.deepcopy(KINGS_AND_ONE_PAWN_GAME_STATE)
        new_game_state.board.apply_move("e2-e3")
        actual = get_possible_moves_for_pawn(new_game_state, "e3")

        expected = {
            "e3-e4"
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_two_kings_one_pawn(self):
        actual = get_possible_moves(KINGS_AND_ONE_PAWN_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e2-e4",
            "e2-e3"
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_two_kings_one_black_pawn(self):
        actual = get_possible_moves(KINGS_AND_ONE_BLACK_PAWN_GAME_STATE)

        expected = {
            "e7-e6",
            "e7-e5",
            "e8-f8",
            "e8-f7",
            "e8-d8",
            "e8-d7",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_white_rook(self):
        actual = get_possible_moves(KINGS_AND_ONE_ROOK_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "a1-a2",
            "a1-a3",
            "a1-a4",
            "a1-a5",
            "a1-a6",
            "a1-a7",
            "a1-a8",
            "a1-b1",
            "a1-c1",
            "a1-d1",
        }

        self.assertEqual(expected, actual)
