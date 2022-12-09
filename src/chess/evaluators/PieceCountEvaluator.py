from chess.evaluators.Evaluator import Evaluator

# TODO maybe factor these out into piece classes?
PIECE_TYPE_TO_POINT_VALUE = {
    "P": 1,
    "B": 3,
    "N": 3,
    "R": 5,
    "Q": 9,
    "K": 0,
}


class PieceCountEvaluator(Evaluator):
    def evaluate(self, game_state) -> float:
        result = 0.0

        for white_piece in game_state.board.get_pieces_for_color("white").values():
            piece_type = white_piece[1]
            piece_value = PIECE_TYPE_TO_POINT_VALUE[piece_type]
            result += piece_value
        for black_piece in game_state.board.get_pieces_for_color("black").values():
            piece_type = black_piece[1]
            piece_value = PIECE_TYPE_TO_POINT_VALUE[piece_type]
            result -= piece_value

        return result
