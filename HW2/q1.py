import math
import time
import numpy as np



class Table(object):
    def __init__(self, points, epsilon, max_dist):
        self._coreset = {}
        self._epsilon = epsilon
        self._points = points
        self._max_dist = max_dist
        self._block_size = epsilon*max_dist # er
        self._dimension = points[0].get_dimension()

        # define the center base point
        self._base_point = points[0]

        # find "top left" point
        dist_vect = Point([self._max_dist for i in range(self._dimension)])
        self._top_left = self._base_point - dist_vect

        # compute size as 2/e
        self._size = int(math.ceil(2 / float(epsilon)))

        # construct_coreset
        self.construct_coreset()

    def construct_coreset(self):
        for point in self._points:
            self.find_slot(point)

    def find_slot(self, point):
        chosen_slot = []
        for coord in (point - self._top_left):
            chosen_slot.append(int(coord/self._block_size))
        self._coreset[tuple(chosen_slot)] = point

    def get_coreset(self):
        return self._coreset.values()

# Main function
def one_center_grid_coreset(points, epsilon):
    # create point objects from input
    points = map(Point, points)

    # choose the first point as u
    chosen_point = points[0]
    furthest_point = chosen_point.furthest_point(points)
    furthest_dist = chosen_point.euclid_dist(furthest_point)

    # now we need to create the table
    coreset_table = Table(points, epsilon, furthest_dist)

    # return the coreset as a list of lists
    return map(Point.get_point_arr, coreset_table.get_coreset())
