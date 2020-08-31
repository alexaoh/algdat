def take_pieces(n_pieces):
    for i in range(1,8):
        if (n_pieces - i) % 8 == 1:
            return i
    return 2
