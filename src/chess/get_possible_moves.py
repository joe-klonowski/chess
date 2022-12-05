import copy

from chess.constants import EIGHT_CARDINAL_DIRECTIONS, FOUR_CARDINAL_DIRECTIONS, FOUR_DIAGONAL_DIRECTIONS, \
    EIGHT_KNIGHT_DIRECTIONS, PIECE_TYPES_PAWN_CAN_PROMOTE_TO
from chess.utils import opposite_color


def get_possible_moves(game_state):
    player_to_move = game_state.player_to_move
    board = game_state.board
    pieces_of_player_to_move = board.get_pieces_for_color(player_to_move)
    result = set()
    for square in pieces_of_player_to_move.keys():
        moves_for_this_piece = get_possible_moves_for_piece(game_state, square)
        result = result.union(moves_for_this_piece)

    if can_castle_queenside(game_state):
        result.add("0-0-0")
    if can_castle_kingside(game_state):
        result.add("0-0")

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
    # TODO maybe break this down into smaller functions?

    pawn_color = game_state.board.get_piece_on_square(square)[0]
    pawn_direction = "N"
    pawn_capture_directions = ["NE", "NW"]
    pawn_promotion_rank = "8"
    en_passant_start_rank = "5"
    if pawn_color == "black":
        pawn_direction = "S"
        pawn_capture_directions = ["SE", "SW"]
        pawn_promotion_rank = "1"
        en_passant_start_rank = "4"
    squares_pawn_can_move_to = set()

    # Check if we can move one square forward
    square_one_space_forward = get_relative_square(square, pawn_direction, 1)
    piece_on_square_one_space_forward = game_state.board.get_piece_on_square(square_one_space_forward)
    rank_one_space_forward = square_one_space_forward[1]
    if piece_on_square_one_space_forward is None:
        squares_pawn_can_move_to.add(square_one_space_forward)

    # Check if we can move two squares forward
    if pawn_is_on_starting_square(pawn_color, square):
        square_two_spaces_forward = get_relative_square(square, pawn_direction, 2)
        piece_on_square_two_spaces_forward = game_state.board.get_piece_on_square(square_two_spaces_forward)
        if piece_on_square_two_spaces_forward is None:
            squares_pawn_can_move_to.add(square_two_spaces_forward)

    # Check for capture moves
    for direction in pawn_capture_directions:
        end_square = get_relative_square(square, direction, 1)
        piece_on_end_square = game_state.board.get_piece_on_square(end_square)
        if piece_on_end_square is not None:
            color_of_piece_on_end_square = piece_on_end_square[0]
            if pawn_color != color_of_piece_on_end_square:
                squares_pawn_can_move_to.add(end_square)

    # Check for en passant
    current_rank = square[1]
    if current_rank == en_passant_start_rank:
        en_passantable_pawn_square = game_state.pawn_that_just_moved_two_squares
        if en_passantable_pawn_square is not None:
            square_west_of_current_square = get_relative_square(square, "W", 1)
            square_east_of_current_square = get_relative_square(square, "E", 1)
            square_to_move_to_en_passant = get_relative_square(en_passantable_pawn_square, pawn_direction, 1)
            if square_west_of_current_square == en_passantable_pawn_square:
                squares_pawn_can_move_to.add(square_to_move_to_en_passant)
            elif square_east_of_current_square == en_passantable_pawn_square:
                squares_pawn_can_move_to.add(square_to_move_to_en_passant)

    result = set()
    if rank_one_space_forward == pawn_promotion_rank:
        for end_square in squares_pawn_can_move_to:
            for piece_type in PIECE_TYPES_PAWN_CAN_PROMOTE_TO:
                result.add(f"{square}-{end_square}={piece_type}")
    else:  # This is not a promotion move
        for end_square in squares_pawn_can_move_to:
            result.add(f"{square}-{end_square}")

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


def can_any_piece_move_to_square(game_state, square):
    for (current_piece_square, piece) in game_state.board.get_pieces_for_color(game_state.player_to_move).items():
        piece_type = piece[1]
        possible_moves_for_piece = GET_POSSIBLE_MOVES_BY_PIECE_TYPE[piece_type](game_state, current_piece_square)
        for move in possible_moves_for_piece:
            destination_square = move[3:5]
            if destination_square == square:
                return True
    return False


def is_king_in_check(game_state):
    opposing_color = "white"
    if game_state.player_to_move == "white":
        opposing_color = "black"
    game_state_with_opposing_color_to_move = copy.deepcopy(game_state)
    game_state_with_opposing_color_to_move.player_to_move = opposing_color
    my_king_square = game_state.board.get_king_square(game_state.player_to_move)
    return can_any_piece_move_to_square(game_state_with_opposing_color_to_move, my_king_square)


GET_POSSIBLE_MOVES_BY_PIECE_TYPE = {
    "K": get_possible_moves_for_king,
    "P": get_possible_moves_for_pawn,
    "R": get_possible_moves_for_rook,
    "B": get_possible_moves_for_bishop,
    "Q": get_possible_moves_for_queen,
    "N": get_possible_moves_for_knight,
}


def get_possible_moves_for_piece(game_state, square):
    piece_on_square = game_state.board.get_piece_on_square(square)
    piece_type = piece_on_square[1]
    # TODO filter out moves that would put the king in check
    return GET_POSSIBLE_MOVES_BY_PIECE_TYPE[piece_type](game_state, square)


def can_castle_queenside(game_state):
    squares_that_must_have_no_pieces = {"b8", "c8", "d8"}
    squares_that_must_not_be_attacked = {"c8", "d8", "e8"}
    if game_state.player_to_move == "white":
        squares_that_must_have_no_pieces = {"b1", "c1", "d1"}
        squares_that_must_not_be_attacked = {"c1", "d1", "e1"}
        if game_state.white_king_has_moved:
            return False
        if game_state.a1_rook_has_moved:
            return False
        if game_state.board.get_piece_on_square("a1") != ("white", "R"):
            return False
    else:  # player to move is black
        if game_state.black_king_has_moved:
            return False
        if game_state.a8_rook_has_moved:
            return False
        if game_state.board.get_piece_on_square("a8") != ("black", "R"):
            return False

    for square in squares_that_must_have_no_pieces:
        if game_state.board.get_piece_on_square(square):
            return False

    game_state_with_opposite_player_to_move = copy.deepcopy(game_state)
    game_state_with_opposite_player_to_move.player_to_move = opposite_color(game_state.player_to_move)
    for square in squares_that_must_not_be_attacked:
        if can_any_piece_move_to_square(game_state_with_opposite_player_to_move, square):
            return False

    return True


def can_castle_kingside(game_state):
    squares_that_must_have_no_pieces = {"f8", "g8"}
    squares_that_must_not_be_attacked = {"e8", "f8", "g8"}
    if game_state.player_to_move == "white":
        squares_that_must_have_no_pieces = {"f1", "g1"}
        squares_that_must_not_be_attacked = {"e1", "f1", "g1"}
        if game_state.white_king_has_moved:
            return False
        if game_state.h1_rook_has_moved:
            return False
        if game_state.board.get_piece_on_square("h1") != ("white", "R"):
            return False
    else:  # player to move is black
        if game_state.black_king_has_moved:
            return False
        if game_state.h8_rook_has_moved:
            return False
        if game_state.board.get_piece_on_square("h8") != ("black", "R"):
            return False

    for square in squares_that_must_have_no_pieces:
        if game_state.board.get_piece_on_square(square):
            return False

    game_state_with_opposite_player_to_move = copy.deepcopy(game_state)
    game_state_with_opposite_player_to_move.player_to_move = opposite_color(game_state.player_to_move)
    for square in squares_that_must_not_be_attacked:
        if can_any_piece_move_to_square(game_state_with_opposite_player_to_move, square):
            return False

    return True
