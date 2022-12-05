import copy
from unittest import TestCase

from chess.get_possible_moves import get_possible_moves, get_possible_moves_for_king, \
    get_relative_square, get_possible_moves_for_pawn, linear_search_for_moves
from constants import KINGS_AND_ONE_PAWN_GAME_STATE, KINGS_AND_ONE_BLACK_PAWN_GAME_STATE, KINGS_AND_ONE_ROOK_GAME_STATE, \
    KING_ROOK_AND_BISHOP_VS_KING_GAME_STATE, KING_AND_ROOK_VS_BISHOP_AND_KING_GAME_STATE, \
    KING_AND_QUEEN_VS_KING_GAME_STATE, KING_AND_KNIGHT_VS_KING_GAME_STATE, KING_AND_KNIGHT_NEAR_EDGE_VS_KING_GAME_STATE, \
    KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_GAME_STATE, GAME_STATE_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT, \
    KING_CAN_CAPTURE_GAME_STATE, PAWN_CAN_CAPTURE_GAME_STATE, PAWN_CANT_CAPTURE_SAME_COLOR_GAME_STATE, \
    PAWN_CAN_PROMOTE_GAME_STATE, PAWN_CAN_CAPTURE_AND_PROMOTE_GAME_STATE


class TestGetPossibleMoves(TestCase):
    # TODO add tests that verify possible moves are removed that would put the king in check,
    # either by moving king into check or by moving a piece that's pinned to the king.
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

    def test_get_possible_moves_where_king_can_capture(self):
        actual = get_possible_moves(KING_CAN_CAPTURE_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_starting_square(self):
        actual = get_possible_moves_for_pawn(KINGS_AND_ONE_PAWN_GAME_STATE, "e2")

        expected = {
            "e2-e3",
            "e2-e4"
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_starting_square_double_move_blocked(self):
        new_game_state = copy.deepcopy(KINGS_AND_ONE_PAWN_GAME_STATE)
        new_game_state.board.add_piece("white", "B", "e4")
        actual = get_possible_moves_for_pawn(new_game_state, "e2")

        expected = {
            "e2-e3",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_including_capture(self):
        actual = get_possible_moves_for_pawn(PAWN_CAN_CAPTURE_GAME_STATE, "d2")

        expected = {
            "d2-d3",
            "d2-d4",
            "d2-e3"
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_cant_capture_same_color_piece(self):
        actual = get_possible_moves_for_pawn(PAWN_CANT_CAPTURE_SAME_COLOR_GAME_STATE, "d2")

        expected = {
            "d2-d3",
            "d2-d4",
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

    def test_get_possible_moves_for_blocked_pawn(self):
        new_game_state = copy.deepcopy(KINGS_AND_ONE_PAWN_GAME_STATE)
        new_game_state.board.apply_move("e2-e3")
        new_game_state.board.add_piece("black", "N", "e4")
        actual = get_possible_moves_for_pawn(new_game_state, "e3")

        self.assertEqual(set(), actual)

    def test_get_possible_moves_for_pawn_that_can_promote(self):
        actual = get_possible_moves_for_pawn(PAWN_CAN_PROMOTE_GAME_STATE, "a7")

        expected = {
            "a7-a8=Q",
            "a7-a8=R",
            "a7-a8=B",
            "a7-a8=N",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_for_pawn_that_can_promote_and_capture(self):
        actual = get_possible_moves_for_pawn(PAWN_CAN_CAPTURE_AND_PROMOTE_GAME_STATE, "a7")

        expected = {
            "a7-a8=Q",
            "a7-a8=R",
            "a7-a8=B",
            "a7-a8=N",
            "a7-b8=Q",
            "a7-b8=R",
            "a7-b8=B",
            "a7-b8=N",
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

    def test_linear_search_for_moves_north_to_same_color_piece(self):
        actual = linear_search_for_moves(KING_ROOK_AND_BISHOP_VS_KING_GAME_STATE, "a1", "N")

        expected = {
            "a1-a2",
            "a1-a3",
            "a1-a4",
            "a1-a5",
            "a1-a6",
        }

        self.assertEqual(expected, actual)

    def test_linear_search_for_moves_north_to_different_color_piece(self):
        actual = linear_search_for_moves(KING_AND_ROOK_VS_BISHOP_AND_KING_GAME_STATE, "a1", "N")

        expected = {
            "a1-a2",
            "a1-a3",
            "a1-a4",
            "a1-a5",
            "a1-a6",
            "a1-a7",
        }

        self.assertEqual(expected, actual)

    def test_linear_search_for_moves_southeast(self):
        actual = linear_search_for_moves(KING_AND_ROOK_VS_BISHOP_AND_KING_GAME_STATE, "a7", "SE")

        expected = {
            "a7-b6",
            "a7-c5",
            "a7-d4",
            "a7-e3",
            "a7-f2",
            "a7-g1",
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

    def test_get_possible_moves_kings_bishop_and_rook(self):
        actual = get_possible_moves(KING_ROOK_AND_BISHOP_VS_KING_GAME_STATE)

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
            "a1-b1",
            "a1-c1",
            "a1-d1",
            "a7-b6",
            "a7-c5",
            "a7-d4",
            "a7-e3",
            "a7-f2",
            "a7-g1",
            "a7-b8",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_queen(self):
        actual = get_possible_moves(KING_AND_QUEEN_VS_KING_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "c3-c2",
            "c3-c1",
            "c3-c4",
            "c3-c5",
            "c3-c6",
            "c3-c7",
            "c3-c8",
            "c3-b3",
            "c3-a3",
            "c3-d3",
            "c3-e3",
            "c3-f3",
            "c3-g3",
            "c3-h3",
            "c3-d2",
            "c3-b4",
            "c3-a5",
            "c3-a1",
            "c3-b2",
            "c3-d4",
            "c3-e5",
            "c3-f6",
            "c3-g7",
            "c3-h8",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_knight_near_middle(self):
        actual = get_possible_moves(KING_AND_KNIGHT_VS_KING_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "c3-d5",
            "c3-e4",
            "c3-e2",
            "c3-d1",
            "c3-b1",
            "c3-a2",
            "c3-a4",
            "c3-b5",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_knight_near_edge(self):
        actual = get_possible_moves(KING_AND_KNIGHT_NEAR_EDGE_VS_KING_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "b1-a3",
            "b1-c3",
            "b1-d2",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_knight_blocked_by_king(self):
        actual = get_possible_moves(KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_GAME_STATE)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "c2-d4",
            "c2-e3",
            "c2-a1",
            "c2-a3",
            "c2-b4",
        }

        self.assertEqual(expected, actual)

    def test_get_possible_moves_kings_and_knight_can_capture_another_piece(self):
        actual = get_possible_moves(GAME_STATE_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT)

        expected = {
            "e1-f1",
            "e1-f2",
            "e1-d1",
            "e1-d2",
            "e1-e2",
            "c2-d4",
            "c2-e3",
            "c2-a1",
            "c2-a3",
            "c2-b4",
        }

        self.assertEqual(expected, actual)
