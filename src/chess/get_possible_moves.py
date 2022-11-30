def get_possible_moves(game_state):
    player_to_move = game_state.player_to_move
    board = game_state.board
    pieces = board.pieces
    pieces_of_player_to_move = board.get_pieces_for_color(player_to_move)
    result = set()
    for piece in pieces_of_player_to_move:
        # TODO
        pass
    return


def get_relative_square(starting_square, direction, number):
    rank = starting_square[1]
    file = starting_square[0]
    new_rank_int = int(rank)
    new_file_ord = ord(file)
    match direction:
        case "N":
            new_rank_int = new_rank_int + number
        case "S":
            new_rank_int = new_rank_int - number
        case "E":
            new_file_ord = new_file_ord + number
        case "W":
            new_file_ord = new_file_ord - number
        case _:
            raise NotImplementedError
    if new_rank_int < 1 or new_rank_int > 8:
        return None
    if new_file_ord < ord("a") or new_file_ord > ord("h"):
        return None
    new_rank = str(new_rank_int)
    new_file = chr(new_file_ord)
    return new_file + new_rank


def get_possible_moves_for_king(game_state, square):
    result = set()
    squares_to_check = set()

    return result


def get_possible_moves_for_pawn(game_state, square):
    pass


def get_possible_moves_for_piece(game_state, square):
    piece_on_square = game_state.board.get_piece_on_square(square)
    piece_type = piece_on_square[1]
    match piece_type:
        case "K":
            return get_possible_moves_for_king(game_state, square)
        case "P":
            return get_possible_moves_for_pawn(game_state, square)
        case _:
            raise ValueError
