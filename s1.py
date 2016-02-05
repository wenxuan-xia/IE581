def midSquare(zi_1):
    """
        input: zi-1
        output: zi
    """
    square = zi_1**2
    square = square//100
    square %= 10000
    return square
