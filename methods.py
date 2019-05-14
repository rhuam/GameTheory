import time
from pprint import pprint
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



if __name__ == "__main__":

    # payoff_matrix = np.array([[(5,0), (5,4), (0,3)],
    #                           [(0,4), (0,3), (5,2)]], dtype='f,f')

    payoff_matrix = np.array([[(-8, -8), (0, -10)],
                              [(-10, 0), (-1, -1)]], dtype='f,f')

    dominant(payoff_matrix, 0)