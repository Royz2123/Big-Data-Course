import time

import k_select
import q1a
import util

def ab_approx(P, k, epsilon):
    output = []

    # find ab approx
    # while we still have points to remove (the rest is constant)
    while int((1-epsilon)*len(P)) > 0:
        # compute the epsilon sample
        sample = q1a.eps_sample(P, epsilon)

        # add representatives to output
        output += sample

        # compute distances for each point
        computed_points = [(
           point,
           util.far_inf(point, sample)
        ) for point in P ]

        # remove (1-eps)n closest points
        top_k, computed_points = k_select.k_select(
            computed_points,
            int((1-epsilon)*len(P)),
            comparer,
            tuple([])
        )

        # for every point left in computed points, add back to P
        P = [p[0] for p in computed_points]

    # return back as list of points
    return output + P

# For this exercise, this is the equivelant of a > b
def comparer(a, b):
    if a[1] <= b[1]:
        return True
    return False

def main():
    test_points = util.generate_random_points(0, 1000, 5001, 2)
    representatives = ab_approx(test_points, 10, 0.1)

    # plot the results
    util.plot_geo_points(test_points)
    util.plot_geo_points(representatives)


if __name__ == "__main__":
    main()
