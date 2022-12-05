import copy

from chess.get_possible_moves import PIECE_TYPE_TO_POSSIBLE_MOVES_FUNCTION


def is_king_in_check(game_state):
    opposing_color = "white"
    if game_state.player_to_move == "white":
        opposing_color = "black"
    game_state_with_opposing_color_to_move = copy.deepcopy(game_state)
    game_state_with_opposing_color_to_move.player_to_move = opposing_color
    my_king_square = game_state.board.get_king_square(game_state.player_to_move)
    for (square, piece) in game_state.board.get_pieces_for_color(opposing_color).items():
        piece_type = piece[1]
        possible_moves_for_piece = PIECE_TYPE_TO_POSSIBLE_MOVES_FUNCTION[piece_type](game_state, square)
        for move in possible_moves_for_piece:
            destination_square = move[3:5]
            if destination_square == my_king_square:
                return True
    return False
