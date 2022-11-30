from dataclasses import dataclass

from chess import ChessBoard


@dataclass
class GameState:
    board: ChessBoard
    player_to_move: str
