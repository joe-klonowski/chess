import copy

from chess import GameState
from chess.utils import opposite_color


def apply_castle_move(game_state, move):
    result = copy.deepcopy(game_state)
    result.player_to_move = opposite_color(game_state.player_to_move)

    switch = (game_state.player_to_move, move)
    if switch == ("white", "0-0"):
        result.board.remove_piece("e1")
        result.board.remove_piece("h1")
        result.board.add_piece("white", "K", "g1")
        result.board.add_piece("white", "R", "f1")
        result.white_king_has_moved = True
        result.h1_rook_has_moved = True
    elif switch == ("white", "0-0-0"):
        result.board.remove_piece("e1")
        result.board.remove_piece("a1")
        result.board.add_piece("white", "K", "c1")
        result.board.add_piece("white", "R", "d1")
        result.white_king_has_moved = True
        result.a1_rook_has_moved = True
    elif switch == ("black", "0-0"):
        result.board.remove_piece("e8")
        result.board.remove_piece("h8")
        result.board.add_piece("black", "K", "g8")
        result.board.add_piece("black", "R", "f8")
        result.black_king_has_moved = True
        result.h8_rook_has_moved = True
    elif switch == ("black", "0-0-0"):
        result.board.remove_piece("e8")
        result.board.remove_piece("a8")
        result.board.add_piece("black", "K", "c8")
        result.board.add_piece("black", "R", "d8")
        result.black_king_has_moved = True
        result.a8_rook_has_moved = True
    return result


def apply_promotion_move(game_state, move):
    result = copy.deepcopy(game_state)
    result.player_to_move = opposite_color(game_state.player_to_move)

    start_square = move[0:2]
    end_square = move[3:5]
    new_piece_type = move[6]

    result.board.remove_piece(start_square)
    result.board.add_piece(game_state.player_to_move, new_piece_type, end_square)

    return result


def apply_move(game_state, move) -> GameState:
    if len(move) > 5 and move[5] == "=":
        return apply_promotion_move(game_state, move)

    if move[0:3] == "0-0":
        return apply_castle_move(game_state, move)

    start_square = move[0:2]
    end_square = move[3:5]

    game_state_copy = copy.deepcopy(game_state)
    piece_moving = game_state_copy.board.remove_piece(start_square)
    piece_color = piece_moving[0]
    piece_type = piece_moving[1]
    game_state_copy.board.add_piece(piece_color, piece_type, end_square)

    game_state_copy.player_to_move = opposite_color(game_state.player_to_move)

    # The rest of the logic updates metadata for tracking whether castling or en passant should be possible
    if piece_type == "K" and piece_color == "white":
        game_state_copy.white_king_has_moved = True
    if piece_type == "K" and piece_color == "black":
        game_state_copy.black_king_has_moved = True
    if piece_type == "P":
        start_rank = int(start_square[1])
        end_rank = int(end_square[1])
        rank_diff = abs(start_rank - end_rank)
        if rank_diff == 2:
            game_state_copy.pawn_that_just_moved_two_squares = end_square
    else:  # Not a pawn move
        game_state_copy.pawn_that_just_moved_two_squares = None
    if piece_type == "R":
        if start_square == "a1":
            game_state_copy.a1_rook_has_moved = True
        if start_square == "a8":
            game_state_copy.a8_rook_has_moved = True
        if start_square == "h1":
            game_state_copy.h1_rook_has_moved = True
        if start_square == "h8":
            game_state_copy.h8_rook_has_moved = True

    return game_state_copy
