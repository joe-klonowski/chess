from chess.GameState import GameState
from chess.ChessBoard import ChessBoard

KINGS_AND_ONE_PAWN_BOARD = ChessBoard()
KINGS_AND_ONE_PAWN_BOARD.add_piece("white", "K", "e1")
KINGS_AND_ONE_PAWN_BOARD.add_piece("black", "K", "e8")
KINGS_AND_ONE_PAWN_BOARD.add_piece("white", "P", "e2")

KINGS_AND_ONE_PAWN_GAME_STATE = GameState(KINGS_AND_ONE_PAWN_BOARD, "white")

KINGS_AND_ONE_BLACK_PAWN_BOARD = ChessBoard()
KINGS_AND_ONE_BLACK_PAWN_BOARD.add_piece("white", "K", "e1")
KINGS_AND_ONE_BLACK_PAWN_BOARD.add_piece("black", "K", "e8")
KINGS_AND_ONE_BLACK_PAWN_BOARD.add_piece("black", "P", "e7")

KINGS_AND_ONE_BLACK_PAWN_GAME_STATE = GameState(KINGS_AND_ONE_BLACK_PAWN_BOARD, "black")

KINGS_AND_ONE_ROOK_BOARD = ChessBoard()
KINGS_AND_ONE_ROOK_BOARD.add_piece("white", "K", "e1")
KINGS_AND_ONE_ROOK_BOARD.add_piece("black", "K", "e8")
KINGS_AND_ONE_ROOK_BOARD.add_piece("white", "R", "a1")

KINGS_AND_ONE_ROOK_GAME_STATE = GameState(KINGS_AND_ONE_ROOK_BOARD, "white")
