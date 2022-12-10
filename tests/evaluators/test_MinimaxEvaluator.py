from unittest import TestCase

from chess.ChessBoard import ChessBoard
from chess.GameState import GameState
from chess.constants import STARTING_GAME_STATE
from chess.evaluators.MinimaxEvaluator import MinimaxEvaluator
from chess.evaluators.PieceCountEvaluator import PieceCountEvaluator


class TestMinimaxEvaluator(TestCase):
    def test_evaluate_starting_position(self):
        piece_count_evaluator = PieceCountEvaluator()
        minimax_evaluator = MinimaxEvaluator(piece_count_evaluator, 1)

        self.assertAlmostEqual(0.0, minimax_evaluator.evaluate(STARTING_GAME_STATE))

    def test_evaluate_can_capture(self):
        board = ChessBoard()
        board.add_piece("white", "K", "e1")
        board.add_piece("black", "K", "e8")
        board.add_piece("white", "P", "a7")
        board.add_piece("black", "R", "b7")
        game_state = GameState(board, "black")
        piece_count_evaluator = PieceCountEvaluator()
        minimax_evaluator = MinimaxEvaluator(piece_count_evaluator, 1)

        self.assertAlmostEqual(-5.0, minimax_evaluator.evaluate(game_state))

    def test_evaluate_trapped_bishop_depth1(self):
        # Insert your own Ian Nepomniachtchi joke here.
        board = ChessBoard()
        board.add_piece("white", "K", "e1")
        board.add_piece("black", "K", "e8")
        board.add_piece("black", "B", "a8")
        board.add_piece("black", "P", "c6")
        board.add_piece("white", "Q", "a7")
        game_state = GameState(board, "black")
        piece_count_evaluator = PieceCountEvaluator()
        minimax_evaluator = MinimaxEvaluator(piece_count_evaluator, 1)

        self.assertAlmostEqual(5.0, minimax_evaluator.evaluate(game_state))

    def test_evaluate_trapped_bishop_depth2(self):
        # Insert your own Ian Nepomniachtchi joke here.
        board = ChessBoard()
        board.add_piece("white", "K", "e1")
        board.add_piece("black", "K", "e8")
        board.add_piece("black", "B", "a8")
        board.add_piece("black", "P", "c6")
        board.add_piece("white", "Q", "a7")
        game_state = GameState(board, "black")
        piece_count_evaluator = PieceCountEvaluator()
        minimax_evaluator = MinimaxEvaluator(piece_count_evaluator, 2)

        self.assertAlmostEqual(8.0, minimax_evaluator.evaluate(game_state))
