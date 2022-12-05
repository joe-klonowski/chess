def opposite_color(color):
    if color == "white":
        return "black"
    elif color == "black":
        return "white"
    else:
        raise ValueError(f"Unrecognized color {color}")