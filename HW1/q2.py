import random

import q1
import util

MAX_SIZE = 2000
MIN_SIZE = 100
STEP = 100

RANGE = 1000
DIMENSION = 3
EPSILON = 0.5


def main():
    for input_size in xrange(MIN_SIZE, MAX_SIZE + STEP, STEP):
        input_points = util.generate_random(0, RANGE, input_size)
        coreset = q1.one_center_grid_coreset(input_points, EPSILON)
        util.plot_points(coreset, input_points)


if __name__ == "__main__":
    main()
