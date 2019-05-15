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
        print(payoff_matrix)


def pareto(payoff_matrix):
    player_sums = list()

    for i in payoff_matrix:
        for s in i:
            player_sums.append((s, (sum(s))))

    player_sums.sort(key=lambda tup: tup[1], reverse=True)

    print([[s[0] for s in player_sums if s[1] == player_sums[0][1]]])