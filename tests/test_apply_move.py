import copy

from unittest import TestCase

from chess.ChessBoard import ChessBoard
from chess.GameState import GameState
from chess.apply_move import apply_move
from chess.constants import STARTING_GAME_STATE


class TestApplyMove(TestCase):
    def test_apply_move_1e4(self):
        actual = apply_move(STARTING_GAME_STATE, "e2-e4")

        expected = copy.deepcopy(STARTING_GAME_STATE)
        expected.board.remove_piece("e2")
        expected.board.add_piece("white", "P", "e4")
        expected.player_to_move = "black"
        expected.pawn_that_just_moved_two_squares = "e4"

        self.assertEqual(expected, actual)

    def test_apply_move_bongcloud(self):
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
        expected.white_king_has_moved = True

        self.assertEqual(expected, actual)

    def test_apply_move_update_rook_moved_metadata(self):
        board = ChessBoard()
        board.add_piece("white", "R", "a1")
        game_state = GameState(board, "white")

        actual_game_state = apply_move(game_state, "a1-a2")

        expected_board = ChessBoard()
        expected_board.add_piece("white", "R", "a2")
        expected_game_state = GameState(expected_board, "black")
        expected_game_state.a1_rook_has_moved = True

        self.assertEqual(expected_game_state, actual_game_state)

    def test_apply_move_white_queenside_castle(self):
        board = ChessBoard()
        board.add_piece("white", "R", "a1")
        board.add_piece("white", "K", "e1")
        game_state = GameState(board, "white")

        actual_game_state = apply_move(game_state, "0-0-0")

        expected_board = ChessBoard()
        expected_board.add_piece("white", "R", "d1")
        expected_board.add_piece("white", "K", "c1")
        expected_game_state = GameState(expected_board, "black")
        expected_game_state.a1_rook_has_moved = True
        expected_game_state.white_king_has_moved = True

        self.assertEqual(expected_game_state, actual_game_state)

    def test_apply_move_white_kingside_castle(self):
        board = ChessBoard()
        board.add_piece("white", "R", "h1")
        board.add_piece("white", "K", "e1")
        game_state = GameState(board, "white")

        actual_game_state = apply_move(game_state, "0-0")

        expected_board = ChessBoard()
        expected_board.add_piece("white", "R", "f1")
        expected_board.add_piece("white", "K", "g1")
        expected_game_state = GameState(expected_board, "black")
        expected_game_state.h1_rook_has_moved = True
        expected_game_state.white_king_has_moved = True

        self.assertEqual(expected_game_state, actual_game_state)

    def test_apply_move_black_kingside_castle(self):
        board = ChessBoard()
        board.add_piece("black", "R", "h8")
        board.add_piece("black", "K", "e8")
        game_state = GameState(board, "black")

        actual_game_state = apply_move(game_state, "0-0")

        expected_board = ChessBoard()
        expected_board.add_piece("black", "R", "f8")
        expected_board.add_piece("black", "K", "g8")
        expected_game_state = GameState(expected_board, "white")
        expected_game_state.h8_rook_has_moved = True
        expected_game_state.black_king_has_moved = True

        self.assertEqual(expected_game_state, actual_game_state)

    def test_apply_move_black_promotion(self):
        board = ChessBoard()
        board.add_piece("black", "P", "h2")
        game_state = GameState(board, "black")

        actual_game_state = apply_move(game_state, "h2-h1=N")

        expected_board = ChessBoard()
        expected_board.add_piece("black", "N", "h1")
        expected_game_state = GameState(expected_board, "white")

        self.assertEqual(expected_game_state, actual_game_state)

    def test_apply_move_white_promotion(self):
        board = ChessBoard()
        board.add_piece("white", "P", "b7")
        game_state = GameState(board, "white")

        actual_game_state = apply_move(game_state, "b7-b8=Q")

        expected_board = ChessBoard()
        expected_board.add_piece("white", "Q", "b8")
        expected_game_state = GameState(expected_board, "black")

        self.assertEqual(expected_game_state, actual_game_state)
