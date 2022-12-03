from chess.constants import EIGHT_CARDINAL_DIRECTIONS, FOUR_CARDINAL_DIRECTIONS, FOUR_DIAGONAL_DIRECTIONS, \
    EIGHT_KNIGHT_DIRECTIONS


def get_possible_moves(game_state):
    player_to_move = game_state.player_to_move
    board = game_state.board
    pieces_of_player_to_move = board.get_pieces_for_color(player_to_move)
    result = set()
    for square in pieces_of_player_to_move.keys():
        moves_for_this_piece = get_possible_moves_for_piece(game_state, square)
        result = result.union(moves_for_this_piece)
    return result


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
        case "NE":
            new_rank_int = new_rank_int + number
            new_file_ord = new_file_ord + number
        case "NW":
            new_rank_int = new_rank_int + number
            new_file_ord = new_file_ord - number
        case "SE":
            new_rank_int = new_rank_int - number
            new_file_ord = new_file_ord + number
        case "SW":
            new_rank_int = new_rank_int - number
            new_file_ord = new_file_ord - number
        # "NNE", "ENE", etc encode the knight's behavior and ignore the number arg
        case "NNE":
            new_rank_int = new_rank_int + 2
            new_file_ord = new_file_ord + 1
        case "ENE":
            new_rank_int = new_rank_int + 1
            new_file_ord = new_file_ord + 2
        case "ESE":
            new_rank_int = new_rank_int - 1
            new_file_ord = new_file_ord + 2
        case "SSE":
            new_rank_int = new_rank_int - 2
            new_file_ord = new_file_ord + 1
        case "SSW":
            new_rank_int = new_rank_int - 2
            new_file_ord = new_file_ord - 1
        case "WSW":
            new_rank_int = new_rank_int - 1
            new_file_ord = new_file_ord - 2
        case "WNW":
            new_rank_int = new_rank_int + 1
            new_file_ord = new_file_ord - 2
        case "NNW":
            new_rank_int = new_rank_int + 2
            new_file_ord = new_file_ord - 1
        case _:
            raise NotImplementedError(f"Unrecognized direction {direction}")
    if new_rank_int < 1 or new_rank_int > 8:
        return None
    if new_file_ord < ord("a") or new_file_ord > ord("h"):
        return None
    new_rank = str(new_rank_int)
    new_file = chr(new_file_ord)
    return new_file + new_rank


def get_possible_moves_for_king(game_state, square):
    possible_end_squares = set()
    for direction in EIGHT_CARDINAL_DIRECTIONS:
        square_in_this_direction = get_relative_square(square, direction, 1)
        if square_in_this_direction is not None:
            possible_end_squares.add(square_in_this_direction)
    result = set()
    for end_square in possible_end_squares:
        if game_state.board.get_piece_on_square(end_square) is None:
            result.add(f"{square}-{end_square}")
        else:  # There is a piece on end_square
            # Check whether piece is the same color as the king (blocking king) or
            # whether it's the opposite color (king can capture)
            piece_on_end_square_color = game_state.board.get_piece_on_square(end_square)[0]
            king_color = game_state.player_to_move
            if king_color != piece_on_end_square_color:
                result.add(f"{square}-{end_square}")
    return result


def pawn_is_on_starting_square(pawn_color, square):
    rank = square[1]
    if pawn_color == "white" and rank == "2":
        return True
    if pawn_color == "black" and rank == "7":
        return True
    return False


def get_possible_moves_for_pawn(game_state, square):
    pawn_color = game_state.board.get_piece_on_square(square)[0]
    pawn_direction = "N"
    if pawn_color == "black":
        pawn_direction = "S"
    result = set()

    # TODO check whether move is blocked by a piece of the same color
    square_one_space_forward = get_relative_square(square, pawn_direction, 1)
    result.add(f"{square}-{square_one_space_forward}")

    if pawn_is_on_starting_square(pawn_color, square):
        square_two_spaces_forward = get_relative_square(square, pawn_direction, 2)
        result.add(f"{square}-{square_two_spaces_forward}")

    # TODO add support for captures and promotions
    return result


def linear_search_for_moves(game_state, square, direction):
    result = set()
    i = 1
    should_check_next_square = True
    while should_check_next_square:
        next_square_to_check = get_relative_square(square, direction, i)
        if next_square_to_check is None:
            return result
        piece_on_next_square_to_check = game_state.board.get_piece_on_square(next_square_to_check)
        if piece_on_next_square_to_check is None:
            result.add(f"{square}-{next_square_to_check}")
            i += 1
        else:  # There is a piece on next_square_to_check
            should_check_next_square = False
            color_of_piece_on_next_square_to_check = piece_on_next_square_to_check[0]
            piece_color = game_state.board.get_piece_on_square(square)[0]
            if color_of_piece_on_next_square_to_check != piece_color:
                result.add(f"{square}-{next_square_to_check}")
    return result


def get_possible_moves_for_rook(game_state, square):
    result = set()
    for direction in FOUR_CARDINAL_DIRECTIONS:
        moves_in_this_direction = linear_search_for_moves(game_state, square, direction)
        result = result.union(moves_in_this_direction)
    return result


def get_possible_moves_for_bishop(game_state, square):
    result = set()
    for direction in FOUR_DIAGONAL_DIRECTIONS:
        moves_in_this_direction = linear_search_for_moves(game_state, square, direction)
        result = result.union(moves_in_this_direction)
    return result


def get_possible_moves_for_queen(game_state, square):
    result = set()
    for direction in EIGHT_CARDINAL_DIRECTIONS:
        moves_in_this_direction = linear_search_for_moves(game_state, square, direction)
        result = result.union(moves_in_this_direction)
    return result


def get_possible_moves_for_knight(game_state, square):
    possible_end_squares = set()
    for direction in EIGHT_KNIGHT_DIRECTIONS:
        end_square = get_relative_square(square, direction, None)
        if end_square is not None:
            possible_end_squares.add(end_square)
    result = set()
    for end_square in possible_end_squares:
        # Check whether move is blocked by a piece of same color.
        piece_on_end_square = game_state.board.get_piece_on_square(end_square)
        if piece_on_end_square is None:
            result.add(f"{square}-{end_square}")
        else:  # There is a piece on end_square
            color_of_piece_on_end_square = piece_on_end_square[0]
            moving_knight_color = game_state.board.get_piece_on_square(square)[0]
            if color_of_piece_on_end_square != moving_knight_color:
                # Capture a piece of opposing color
                result.add(f"{square}-{end_square}")
    return result


def get_possible_moves_for_piece(game_state, square):
    piece_on_square = game_state.board.get_piece_on_square(square)
    piece_type = piece_on_square[1]
    # TODO filter out moves that would put the king in check
    match piece_type:
        case "K":
            return get_possible_moves_for_king(game_state, square)
        case "P":
            return get_possible_moves_for_pawn(game_state, square)
        case "R":
            return get_possible_moves_for_rook(game_state, square)
        case "B":
            return get_possible_moves_for_bishop(game_state, square)
        case "Q":
            return get_possible_moves_for_queen(game_state, square)
        case "N":
            return get_possible_moves_for_knight(game_state, square)
        case _:
            raise ValueError(f"Unsupported piece type {piece_type}")
