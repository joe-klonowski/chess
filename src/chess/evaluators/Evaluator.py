from abc import ABC, abstractmethod


class Evaluator(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(game_state) -> float:
        """
        :return: a float representing the evaluation of the position. Higher numbers indicate a better
        position for white.
        An evaluation of float('inf') means white has won or will win with perfect play.
        float('-inf') means black has won or will win with perfect play.
        0.0 means the position is a draw with perfect play.
        1.0 means white is ahead by about one pawn.
        -1.0 means black is ahead by about one pawn.
        """
        raise NotImplementedError
