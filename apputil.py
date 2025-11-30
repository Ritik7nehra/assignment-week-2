import numpy as np

def ways(cents, coin_types=[1, 5]):
    """
    Return number of ways to make `cents` using coin_types (DP).
    Robust to cents being int-like (will cast to int).
    """
    cents = int(cents)
    if cents < 0:
        return 0

    dp = [0] * (cents + 1)
    dp[0] = 1

    for coin in coin_types:
        coin = int(coin)
        if coin <= 0:
            continue
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]

    return dp[cents]


def lowest_score(names, scores):
    """
    Return the NAME (Python str) of the student with the lowest score.
    Accepts names/scores as Python lists or numpy arrays.
    """
    names_np = np.array(names)
    scores_np = np.array(scores)

    # argmin returns a numpy scalar index; cast to int to be safe
    idx = int(np.argmin(scores_np))
    # .item() converts numpy scalar (including numpy.str_) to Python native
    return names_np[idx].item()


def sort_names(names, scores):
    """
    Return a Python list of names sorted by descending scores.
    Works whether names/scores are lists or numpy arrays.
    """
    names_np = np.array(names)
    scores_np = np.array(scores)

    order = np.argsort(scores_np)[::-1]   # indices for descending order
    sorted_names = names_np[order]
    return sorted_names.tolist()
