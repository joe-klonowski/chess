from chess.apply_move import apply_move
from chess.evaluators.Evaluator import Evaluator
from chess.get_possible_moves import get_possible_moves


class MinimaxEvaluator(Evaluator):
    def __init__(self, base_evaluator, search_depth):
        self.base_evaluator = base_evaluator
        self.search_depth = search_depth

    def evaluate(self, game_state) -> float:
        if self.search_depth == 0:
            return self.base_evaluator.evaluate(game_state)

        # TODO add check for end conditions

        best_score_so_far = float("-inf")
        if game_state.player_to_move == "black":
            best_score_so_far = float("inf")

        possible_moves = get_possible_moves(game_state)
        for move in possible_moves:
            # TODO optimize this; don't create a new evaluator object for each recursive call.
            # Would be good to do memoization as well.
            recursive_evaluator = MinimaxEvaluator(self.base_evaluator, self.search_depth - 1)
            new_game_state = apply_move(game_state, move)
            evaluation = recursive_evaluator.evaluate(new_game_state)
            if \
                    (game_state.player_to_move == "white" and evaluation > best_score_so_far) or \
                    (game_state.player_to_move == "black" and evaluation < best_score_so_far):
                best_score_so_far = evaluation

        return best_score_so_far


