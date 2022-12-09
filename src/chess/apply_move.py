import copy

from chess import GameState
from chess.constants import STARTING_GAME_STATE
from chess.utils import opposite_color


def apply_move(game_state, move) -> GameState:
    start_square = move[0:2]
    end_square = move[3:5]

    game_state_copy = copy.deepcopy(game_state)
    piece_moving = game_state_copy.board.remove_piece(start_square)
    piece_color = piece_moving[0]
    piece_type = piece_moving[1]
    game_state_copy.board.add_piece(piece_color, piece_type, end_square)

    game_state_copy.player_to_move = opposite_color(game_state.player_to_move)

    # TODO update a few more metadata things in game_state like whether kings have moved.

    return game_state_copy
