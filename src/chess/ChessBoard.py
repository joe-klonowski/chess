class ChessBoard:
    white_king_square = None
    black_king_square = None

    def __init__(self):
        self.pieces = dict()

    def add_piece(self, color, piece, square):
        self.pieces.update({square: (color, piece)})
        if piece == "K" and color == "white":
            self.white_king_square = square
        elif piece == "K" and color == "black":
            self.black_king_square = square

    def remove_piece(self, square) -> None:
        self.pieces.pop(square)

    def get_pieces(self):
        return self.pieces

    def get_piece_on_square(self, square):
        return self.pieces.get(square)

    def apply_move(self, move):
        # TODO implement castling, promotion, en passant
        starting_square = move[0:2]
        piece_type = self.get_piece_on_square(starting_square)
        ending_square = move[3:5]
        self.pieces.update({starting_square: None, ending_square: piece_type})

    def get_pieces_for_color(self, color):
        result = dict()
        for item in self.pieces.items():
            piece = item[1]
            current_item_color = piece[0]
            if current_item_color == color:
                square = item[0]
                result.update({square: piece})
        return result

    def get_king_square(self, color):
        if color == "white":
            return self.white_king_square
        else:
            return self.black_king_square

    def __eq__(self, other):
        return self.pieces == other.pieces
