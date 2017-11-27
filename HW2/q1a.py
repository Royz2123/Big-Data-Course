import math
import time

import util

# Function required in Question 1
def eps_sample(P, epsilon):
    # split into (1/e)^d groups
    groups = recur_eps_sample(P, epsilon, 0, len(P[0]))

    # find representative for each group
    return [if len(group) group[0] for group in groups]


# call this recursively
def recur_eps_sample(groups, epsilon, dim, max_dim):
    if dim == max_dim:
        return groups

    new_groups = []
    # loop through all the groups
    for group in groups:
        while not len(group):
            new_groups.append(util.k_select(
                group,
                len(group)*epsilon,
                comparer,
                [index]
            ))

    # finally return the recursive call on dim+1
    return recur_eps_sample(new_groups, epsilon, dim+1, max_dim)

def comparer(a, b, index):
    if a[index] > b[index]:
        return a
    return b
