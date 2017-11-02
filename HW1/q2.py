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
    x_values = []
    y_values = []

    for input_size in xrange(MIN_SIZE, MAX_SIZE + STEP, STEP):
        # generate the input points
        input_points = util.generate_random_points(
            0,
            RANGE,
            input_size,
            DIMENSION
        )

        # generate coreset
        coreset = q1.one_center_grid_coreset(input_points, EPSILON)

        # update the size of the coreset
        x_values.append(len(coreset))
        y_values.append(input_size)

    # plot the results
    util.plot_points(x_values, y_values, "coreset size", "input size")


if __name__ == "__main__":
    main()
