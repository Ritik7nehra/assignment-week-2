import numpy as np

def ways(cents, coin_types=[1, 5]):
    """
    Calculate the number of ways to make change for a given amount using coins.
    """
    dp = [0] * (cents + 1)
    dp[0] = 1  # Base case

    for coin in coin_types:
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]

    return dp[cents]


import numpy as np

def lowest_score(names, scores):
    # Find the index of the minimum score
    idx = np.argmin(scores)
    # Return the corresponding student name
    return names[idx]


def sort_names(names, scores):
    # Get indices that would sort the scores in descending order
    sorted_idx = np.argsort(scores)[::-1]
    # Reorder names based on those indices
    return names[sorted_idx]
