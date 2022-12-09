from unittest import TestCase

from chess.constants import STARTING_GAME_STATE
from chess.evaluators.NaiveEvaluator import NaiveEvaluator


class TestNaiveEvaluator(TestCase):
    def test_evaluate(self):
        evaluator = NaiveEvaluator()
        self.assertEqual(0.0, evaluator.evaluate(STARTING_GAME_STATE))
