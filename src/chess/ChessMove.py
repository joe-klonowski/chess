from dataclasses import dataclass

from chess.pieces import ChessPiece


@dataclass
class ChessMove:
    """
    For example, starting move pawn e2-e4:
    ChessMove(ChessPiece(
    """
    starting_pieces: list[ChessPiece]
    ending_pieces: list[ChessPiece]
