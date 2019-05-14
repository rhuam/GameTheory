import numpy as np

## Solution by dominant action
def dominant(payoff_matrix, player):

    payoff_matrix = payoff_matrix.transpose()       # Swap payoff player
    player = 1 - player                             # Swap player (0, 1)

    s = list()

    for i in payoff_matrix:
        player_ratings = [j[player] for j in i]
        s.append(max(player_ratings))

    mask = np.array([i-min(s) for i in s], dtype=bool)

    if mask.any(0):
        payoff_matrix = payoff_matrix[mask]
        dominant(payoff_matrix, player)
    else:
        print(payoff_matrix)

