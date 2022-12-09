from chess.get_possible_moves import is_king_in_check, get_possible_moves


def is_checkmate(game_state) -> bool:
    return is_king_in_check(game_state) and get_possible_moves(game_state) == set()


def is_stalemate(game_state) -> bool:
    return not is_king_in_check(game_state) and get_possible_moves(game_state) == set()
