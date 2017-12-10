import q1a

def ab_approx(P, k, epsilon):
    output = []

    while len(P):
        # computee the epsilon sample
        sample = q1a.eps_sample(P, epsilon)

        # add representatives to output
        output += sample

        # compute distances
        dists = {}
        for point in P:
            dists[point] = util.far_inf(point, sample)

        # remove (1-eps)n closest points
        k_select.k_select(
            P,
            int(1-epsilon)*len(P),
            comparer,
            [dists]
        )

# For this exercise, this is the equivelant of a > b
def comparer(a, b, dists):
    if dists[a] > dists[b]:
        return True
    return False
