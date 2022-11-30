from chess.GameState import GameState
from chess.ChessBoard import ChessBoard

KINGS_AND_ONE_PAWN_BOARD = ChessBoard()
KINGS_AND_ONE_PAWN_BOARD.add_piece("white", "K", "e1")
KINGS_AND_ONE_PAWN_BOARD.add_piece("black", "K", "e8")
KINGS_AND_ONE_PAWN_BOARD.add_piece("white", "P", "e2")

KINGS_AND_ONE_PAWN_GAME_STATE = GameState(KINGS_AND_ONE_PAWN_BOARD, "white")
