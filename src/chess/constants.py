from chess.ChessBoard import ChessBoard


def build_starting_board():
    board = ChessBoard()
    board.add_piece("R", "a1")
    board.add_piece("N", "b1")
    board.add_piece("B", "c1")
    board.add_piece("Q", "d1")
    board.add_piece("K", "e1")
    board.add_piece("B", "f1")
    board.add_piece("N", "g1")
    board.add_piece("R", "h1")
    board.add_piece("P", "a2")
    board.add_piece("P", "b2")
    board.add_piece("P", "c2")
    board.add_piece("P", "d2")
    board.add_piece("P", "e2")
    board.add_piece("P", "f2")
    board.add_piece("P", "g2")
    board.add_piece("P", "h2")
    board.add_piece("R", "a8")
    board.add_piece("N", "b8")
    board.add_piece("B", "c8")
    board.add_piece("Q", "d8")
    board.add_piece("K", "e8")
    board.add_piece("B", "f8")
    board.add_piece("N", "g8")
    board.add_piece("R", "h8")
    board.add_piece("P", "a7")
    board.add_piece("P", "b7")
    board.add_piece("P", "c7")
    board.add_piece("P", "d7")
    board.add_piece("P", "e7")
    board.add_piece("P", "f7")
    board.add_piece("P", "g7")
    board.add_piece("P", "h7")
    return board


STARTING_BOARD = build_starting_board()