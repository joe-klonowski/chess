from chess.evaluators.Evaluator import Evaluator


class NaiveEvaluator(Evaluator):
    def evaluate(self, game_state) -> float:
        return 0.0  # lol
