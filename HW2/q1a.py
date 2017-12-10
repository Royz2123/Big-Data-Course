import math
import time

import k_select
import util

# Function required in Question 1
def eps_sample(P, epsilon):
    # split into (1/e)^d groups
    groups = recur_eps_sample([P], epsilon, 0, len(P[0]))

    # find representative for each group
    return [group[0] for group in groups]

# call this recursively
def recur_eps_sample(groups, epsilon, dim, max_dim):
    if dim == max_dim:
        return groups

    new_groups = []
    # loop through all the groups
    for group in groups:
        # copy group into a workable set
        working_group = group[:]

        # split this group into sets of k
        while len(working_group):
            top_k, working_group = k_select.k_select(
                working_group,
                int(len(group)*epsilon),
                comparer,
                tuple([dim])
            )
            new_groups.append(top_k)

    # finally return the recursive call on dim+1
    return recur_eps_sample(new_groups, epsilon, dim+1, max_dim)

# For this exercise, this is the equivelant of a > b
def comparer(a, b, index):
    if a[index] > b[index]:
        return True
    return False

def main():
    test_points = util.generate_random_points(0, 1000, 500, 2)
    representatives = eps_sample(test_points, 0.2)

    # plot the results
    util.plot_geo_points(test_points)
    util.plot_geo_points(representatives)


if __name__ == "__main__":
    main()
