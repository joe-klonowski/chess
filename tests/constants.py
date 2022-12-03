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

KING_ROOK_AND_BISHOP_VS_KING_BOARD = ChessBoard()
KING_ROOK_AND_BISHOP_VS_KING_BOARD.add_piece("white", "K", "e1")
KING_ROOK_AND_BISHOP_VS_KING_BOARD.add_piece("black", "K", "e8")
KING_ROOK_AND_BISHOP_VS_KING_BOARD.add_piece("white", "R", "a1")
KING_ROOK_AND_BISHOP_VS_KING_BOARD.add_piece("white", "B", "a7")

KING_ROOK_AND_BISHOP_VS_KING_GAME_STATE = GameState(KING_ROOK_AND_BISHOP_VS_KING_BOARD, "white")

KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD = ChessBoard()
KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD.add_piece("white", "K", "e1")
KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD.add_piece("black", "K", "e8")
KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD.add_piece("white", "R", "a1")
KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD.add_piece("black", "B", "a7")

KING_AND_ROOK_VS_BISHOP_AND_KING_GAME_STATE = GameState(KING_AND_ROOK_VS_BISHOP_AND_KING_BOARD, "white")
