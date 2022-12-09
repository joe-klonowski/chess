from chess.evaluators.Evaluator import Evaluator


class NaiveEvaluator(Evaluator):
    @staticmethod
    def evaluate(game_state) -> float:
        return 0.0  # lol
