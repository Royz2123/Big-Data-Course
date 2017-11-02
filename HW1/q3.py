import q1
import util

INPUT_SIZE = 2000
DIMENSION = 2

# divide by 10 later
MAX_EPSILON = 10
MIN_EPSILON = 1
STEP = 1

Q_SIZE = 100
Q_RANGE = 10000


def coreset_worth(test, input_points, coreset):
    # create point objects
    input_points = map(q1.Point, input_points)
    coreset = map(q1.Point, coreset)

    # find maximal q
    return max([test_coreset(point, input_points, coreset) for point in test])

def test_coreset(test_point, input_points, coreset):
    # create a Point object
    test_point = q1.Point(test_point)

    # find distances as in equation from coreset and original input
    dist_pq = test_point.euclid_dist(test_point.furthest_point(input_points))
    dist_cq = test_point.euclid_dist(test_point.furthest_point(coreset))

    #return coreset worth for this test_point
    return (dist_pq - dist_cq)/dist_pq


def main():
    # plotting values
    x_values = []
    y_values = []

    # generate input points
    input_points = util.generate_random_points(0, Q_RANGE, INPUT_SIZE, DIMENSION)

    # find coreset for each input size
    for epsilon in xrange(MIN_EPSILON, MAX_EPSILON + STEP, STEP):
        # real epsilon
        epsilon = epsilon/10.0

        # compute coreset
        coreset = q1.one_center_grid_coreset(input_points, epsilon)

        # generate Q
        q_points = util.generate_random_points(0, Q_RANGE, Q_SIZE, DIMENSION)

        # compute mi
        mi = coreset_worth(q_points, input_points, coreset)

        # document results
        x_values.append(mi)
        y_values.append(epsilon)

    util.plot_points(x_values, y_values, "error", "epsilon")


if __name__ == "__main__":
    main()
