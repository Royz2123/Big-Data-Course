import q1
import util

INPUT_SIZE = 2000
DIMENSION = 3

MAX_EPSILON = 1.0
MIN_EPSILON = 0.1
STEP = 0.1

Q_SIZE = 100
Q_RANGE = 10000


def coreset_worth(test, input_points, coreset):
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
    input_points = util.generate_random(0, Q_RANGE, INPUT_SIZE)

    for epsilon in xrange(MIN_EPSILON, MAX_EPSILON + STEP, STEP):
        coreset = q1.one_center_grid_coreset(input_points, epsilon)

        # generate Q
        q_points = util.generate_random(0, Q_RANGE, Q_SIZE)

        # compute mi
        mi = coreset_worth(q_points, input_points, coreset)
        util.plot_points(mi, epsilon)


if __name__ == "__main__":
    main()
