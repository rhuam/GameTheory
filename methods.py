import numpy as np

## Solution by dominant action
def dominant(payoff_matrix, player):

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
        dominant(payoff_matrix, player)
    else:
        print(payoff_matrix)


if __name__ == "__main__":

    payoff_matrix = np.array([[(5,0), (5,4), (0,3)],
                              [(0,4), (0,3), (5,2)]], dtype='f,f')

    # payoff_matrix = np.array([[(-8, -8), (0, -10)],
    #                           [(-10, 0), (-1, -1)]], dtype='f,f')

    dominant(payoff_matrix, 0)