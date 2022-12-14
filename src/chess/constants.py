from chess.ChessBoard import ChessBoard
from chess.GameState import GameState


def build_starting_board():
    board = ChessBoard()
    board.add_piece("white", "R", "a1")
    board.add_piece("white", "N", "b1")
    board.add_piece("white", "B", "c1")
    board.add_piece("white", "Q", "d1")
    board.add_piece("white", "K", "e1")
    board.add_piece("white", "B", "f1")
    board.add_piece("white", "N", "g1")
    board.add_piece("white", "R", "h1")
    board.add_piece("white", "P", "a2")
    board.add_piece("white", "P", "b2")
    board.add_piece("white", "P", "c2")
    board.add_piece("white", "P", "d2")
    board.add_piece("white", "P", "e2")
    board.add_piece("white", "P", "f2")
    board.add_piece("white", "P", "g2")
    board.add_piece("white", "P", "h2")
    board.add_piece("black", "R", "a8")
    board.add_piece("black", "N", "b8")
    board.add_piece("black", "B", "c8")
    board.add_piece("black", "Q", "d8")
    board.add_piece("black", "K", "e8")
    board.add_piece("black", "B", "f8")
    board.add_piece("black", "N", "g8")
    board.add_piece("black", "R", "h8")
    board.add_piece("black", "P", "a7")
    board.add_piece("black", "P", "b7")
    board.add_piece("black", "P", "c7")
    board.add_piece("black", "P", "d7")
    board.add_piece("black", "P", "e7")
    board.add_piece("black", "P", "f7")
    board.add_piece("black", "P", "g7")
    board.add_piece("black", "P", "h7")
    return board


STARTING_BOARD = build_starting_board()

STARTING_GAME_STATE = GameState(STARTING_BOARD, "white")

FOUR_CARDINAL_DIRECTIONS = ["N", "E", "S", "W"]
FOUR_DIAGONAL_DIRECTIONS = ["NE", "SE", "SW", "NW"]
EIGHT_CARDINAL_DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
EIGHT_KNIGHT_DIRECTIONS = ["NNE", "ENE", "ESE", "SSE", "SSW", "WSW", "WNW", "NNW"]

PIECE_TYPES_PAWN_CAN_PROMOTE_TO = {"R", "N", "B", "Q"}
