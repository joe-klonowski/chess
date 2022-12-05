from dataclasses import dataclass

from chess import ChessBoard


@dataclass
class GameState:
    board: ChessBoard
    player_to_move: str

    # Can be None or a square like "a5". For checking whether en passant is possible.
    pawn_that_just_moved_two_squares: str = None

    # The rest of these are for determining whether castling is possible.
    white_king_has_moved: bool = False
    black_king_has_moved: bool = False
    a8_rook_has_moved: bool = False
    a1_rook_has_moved: bool = False
    h8_rook_has_moved: bool = False
    h1_rook_has_moved: bool = False
