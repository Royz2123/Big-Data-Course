import random
import numpy as np
import matplotlib.pyplot as plt


def plot_points(x_values, y_values, x_name="", y_name=""):
    plt.scatter(x_values, y_values)
    plt.ylabel(y_name)
    plt.xlabel(x_name)
    plt.show()

def generate_random(min_val, max_val, size):
    return [(random.random()*max_val + min_val) for i in xrange(size)]

def generate_random_points(min_val, max_val, size, dimension=3):
    points = []
    for i in xrange(size):
        points.append(generate_random(min_val, max_val, dimension))
    return points

class Point(object):
    def __init__(self, point_arr):
        self._coords = map(float, point_arr)

    def get_dimension(self):
        return len(self._coords)

    def get_point_arr(self):
        return self._coords

    def __getitem__(self, arg):
        return self._coords[arg]

    def __sub__(self, other):
        vect = []
        for coord in range(len(self._coords)):
            vect.append(self._coords[coord] - other._coords[coord])
        return Point(vect)

    def __add__(self, other):
        vect = []
        for coord in range(len(self._coords)):
            vect.append(self._coords[coord] + other._coords[coord])
        return Point(vect)

    def euclid_dist(self, other):
        dist = 0
        for coord_index in range(len(self._coords)):
            dist += (self._coords[coord_index] - other._coords[coord_index])**2
        return math.sqrt(dist)

    def farther_point(self, point1, point2):
        if (self.euclid_dist(point1) > self.euclid_dist(point2)):
            return point1
        return point2

    def furthest_point(self, points):
        return reduce(
            (
                lambda point1, point2 : point1 if (
                    self.euclid_dist(point1) > self.euclid_dist(point2)
                ) else point2
            ),
            points
        )

    def __repr__(self):
        return "Point Object:\t%s" % self._coords
