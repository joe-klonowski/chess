import copy
from unittest import TestCase

from chess.constants import STARTING_GAME_STATE
from chess.evaluators.PieceCountEvaluator import PieceCountEvaluator


class TestNaiveEvaluator(TestCase):
    def test_evaluate_starting_position(self):
        evaluator = PieceCountEvaluator()
        self.assertAlmostEqual(0.0, evaluator.evaluate(STARTING_GAME_STATE))

    def test_evaluate_starting_position_white_down_pawn(self):
        game_state = copy.deepcopy(STARTING_GAME_STATE)
        game_state.board.remove_piece("e2")

        evaluator = PieceCountEvaluator()

        self.assertAlmostEqual(-1.0, evaluator.evaluate(game_state))

    def test_evaluate_starting_position_white_up_queen(self):
        game_state = copy.deepcopy(STARTING_GAME_STATE)
        game_state.board.remove_piece("d8")

        evaluator = PieceCountEvaluator()

        self.assertAlmostEqual(9.0, evaluator.evaluate(game_state))
