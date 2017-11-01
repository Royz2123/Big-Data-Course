import random

import q1

MAX_SIZE = 2000
MIN_SIZE = 100
STEP = 100

RANGE = 1000
DIMENSION = 3
EPSILON = 0.5

def plot_coreset(coreset, input):
    pass


def main():
    for input_size in xrange(MIN_SIZE, MAX_SIZE + STEP, STEP):
        input_points = [random.random()*RANGE for i in xrange(input_size)]
        coreset = q1.one_center_grid_coreset(input_points, EPSILON)
        plot_coreset(coreset, input_points)


if __name__ == "__main__":
    main()
