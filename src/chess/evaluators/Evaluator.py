from abc import ABC, abstractmethod


class Evaluator(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(game_state) -> float:
        raise NotImplementedError
