import numpy as np

## Solution by dominant action
def dominant(payoff_matrix, player = 0):

    payoff_matrix = payoff_matrix.transpose()       # Swap payoff player
    player = 1 - player                             # Swap player (0, 1)

    s = list()

    # create player ratings vector
    for i in payoff_matrix:
        player_ratings = [j[player] for j in i]
        s.append(max(player_ratings))

    # Subtracted the smallest value from the list of all values to create a cut mask.
    mask = np.array([i-min(s) for i in s], dtype=bool)

    # If it has at least one dominance (zero) continues. If all is zero, the values are equal,
    # so there is no dominance.
    if mask.any(0) and not mask.all(0):
        payoff_matrix = payoff_matrix[mask]
        return dominant(payoff_matrix, player)
    else:
        print(list(payoff_matrix))


def pareto(payoff_matrix):

    mask = np.full(payoff_matrix.shape, False, dtype='bool')

    for line, _ in enumerate(payoff_matrix):
        for col, sx in enumerate(_):

            for i in payoff_matrix:
                for j in i:
                    mask[line][col] = sx[0] >= j[0] and sx[1] >= j[1]


    print(payoff_matrix[mask])


def nash(payoff_matrix):
    # mask = np.full(payoff_matrix.shape, False, dtype='bool')
    mask = payoff_matrix.astype('bool, bool')
    mask.fill(False)

    for line, _ in enumerate(payoff_matrix):
        for col, sx in enumerate(_):
            slice_line = list(payoff_matrix[line])
            slice_col = list(payoff_matrix[:, col])

            mask[line][col][0] = sx[0] >= max(slice_line, key=lambda tup: tup[1])[1]
            mask[line][col][1] = sx[1] >= max(slice_col, key=lambda tup: tup[0])[0]

    new_mask = np.full(payoff_matrix.shape, False, dtype='bool')
    for line, _ in enumerate(payoff_matrix):
        for col, sx in enumerate(_):

            new_mask[line][col] = mask[line][col][0] and mask[line][col][1]

    print(payoff_matrix[new_mask])



if __name__ == "__main__":

    payoff_prisoners_dilemma = np.array([[(-8, -8), (0, -10)],
                                        [(-10, 0), (-1, -1)]], dtype='f,f')

    payoff_matrix = np.array([[(5, 0), (5, 4), (0, 3)],
                              [(5, 5), (0, 3), (5, 2)]], dtype='f,f')
    # dominant(payoff_prisoners_dilemma, 0)

    pareto(payoff_prisoners_dilemma)