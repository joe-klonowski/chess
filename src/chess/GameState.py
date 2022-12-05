from dataclasses import dataclass

from chess import ChessBoard


@dataclass
class GameState:
    board: ChessBoard
    player_to_move: str

    # Can be None or a square like "a5". For checking whether en passant is possible.
    pawn_that_just_moved_two_squares: str

    def __init__(self, board, player_to_move, pawn_that_just_moved_two_squares=None):
        self.board = board
        self.player_to_move = player_to_move
        self.pawn_that_just_moved_two_squares = pawn_that_just_moved_two_squares
