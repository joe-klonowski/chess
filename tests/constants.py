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

KING_CAN_CAPTURE_BOARD = ChessBoard()
KING_CAN_CAPTURE_BOARD.add_piece("white", "K", "e1")
KING_CAN_CAPTURE_BOARD.add_piece("black", "K", "e8")
KING_CAN_CAPTURE_BOARD.add_piece("black", "P", "d2")

KING_CAN_CAPTURE_GAME_STATE = GameState(KING_CAN_CAPTURE_BOARD, "white")

PAWN_CAN_CAPTURE_BOARD = ChessBoard()
PAWN_CAN_CAPTURE_BOARD.add_piece("white", "K", "e1")
PAWN_CAN_CAPTURE_BOARD.add_piece("black", "K", "e8")
PAWN_CAN_CAPTURE_BOARD.add_piece("white", "P", "d2")
PAWN_CAN_CAPTURE_BOARD.add_piece("black", "R", "e3")

PAWN_CAN_CAPTURE_GAME_STATE = GameState(PAWN_CAN_CAPTURE_BOARD, "white")

PAWN_CANT_CAPTURE_SAME_COLOR_BOARD = ChessBoard()
PAWN_CANT_CAPTURE_SAME_COLOR_BOARD.add_piece("white", "K", "e1")
PAWN_CANT_CAPTURE_SAME_COLOR_BOARD.add_piece("black", "K", "e8")
PAWN_CANT_CAPTURE_SAME_COLOR_BOARD.add_piece("white", "P", "d2")
PAWN_CANT_CAPTURE_SAME_COLOR_BOARD.add_piece("white", "R", "e3")

PAWN_CANT_CAPTURE_SAME_COLOR_GAME_STATE = GameState(PAWN_CANT_CAPTURE_SAME_COLOR_BOARD, "white")

PAWN_CAN_PROMOTE_BOARD = ChessBoard()
PAWN_CAN_PROMOTE_BOARD.add_piece("white", "K", "e1")
PAWN_CAN_PROMOTE_BOARD.add_piece("black", "K", "e8")
PAWN_CAN_PROMOTE_BOARD.add_piece("white", "P", "a7")

PAWN_CAN_PROMOTE_GAME_STATE = GameState(PAWN_CAN_PROMOTE_BOARD, "white")

PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD = ChessBoard()
PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD.add_piece("white", "K", "e1")
PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD.add_piece("black", "K", "e8")
PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD.add_piece("white", "P", "a7")
PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD.add_piece("black", "B", "b8")

PAWN_CAN_CAPTURE_AND_PROMOTE_GAME_STATE = GameState(PAWN_CAN_CAPTURE_AND_PROMOTE_BOARD, "white")

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

KING_AND_QUEEN_VS_KING_BOARD = ChessBoard()
KING_AND_QUEEN_VS_KING_BOARD.add_piece("white", "K", "e1")
KING_AND_QUEEN_VS_KING_BOARD.add_piece("black", "K", "e8")
KING_AND_QUEEN_VS_KING_BOARD.add_piece("white", "Q", "c3")

KING_AND_QUEEN_VS_KING_GAME_STATE = GameState(KING_AND_QUEEN_VS_KING_BOARD, "white")

KING_AND_KNIGHT_VS_KING_BOARD = ChessBoard()
KING_AND_KNIGHT_VS_KING_BOARD.add_piece("white", "K", "e1")
KING_AND_KNIGHT_VS_KING_BOARD.add_piece("black", "K", "e8")
KING_AND_KNIGHT_VS_KING_BOARD.add_piece("white", "N", "c3")

KING_AND_KNIGHT_VS_KING_GAME_STATE = GameState(KING_AND_KNIGHT_VS_KING_BOARD, "white")

KING_AND_KNIGHT_NEAR_EDGE_VS_KING_BOARD = ChessBoard()
KING_AND_KNIGHT_NEAR_EDGE_VS_KING_BOARD.add_piece("white", "K", "e1")
KING_AND_KNIGHT_NEAR_EDGE_VS_KING_BOARD.add_piece("black", "K", "e8")
KING_AND_KNIGHT_NEAR_EDGE_VS_KING_BOARD.add_piece("white", "N", "b1")

KING_AND_KNIGHT_NEAR_EDGE_VS_KING_GAME_STATE = GameState(KING_AND_KNIGHT_NEAR_EDGE_VS_KING_BOARD, "white")

KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_BOARD = ChessBoard()
KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_BOARD.add_piece("white", "K", "e1")
KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_BOARD.add_piece("black", "K", "e8")
KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_BOARD.add_piece("white", "N", "c2")

KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_GAME_STATE = GameState(KING_AND_KNIGHT_BLOCKED_BY_KING_VS_KING_BOARD, "white")

BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT = ChessBoard()
BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT.add_piece("white", "K", "e1")
BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT.add_piece("black", "K", "e8")
BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT.add_piece("white", "N", "c2")
BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT.add_piece("black", "Q", "e3")

GAME_STATE_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT = GameState(BOARD_WITH_POSSIBLE_CAPTURE_MOVE_FOR_KNIGHT, "white")
