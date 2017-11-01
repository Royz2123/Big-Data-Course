import math

class Point(object):
    def __init__(self, point_arr):
        self._coords = map(float, point_arr)

    def get_dimension(self):
        return len(self._coords)

    def get_point_arr(self):
        return self._coords

    def euclid_dist(self, other):
        dist = 0
        for coord_index in range(len(self._coords)):
            dist += (self._coords[coord_index] - other._coords[coord_index])**2
        return dist

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


class Table(object):
    def __init__(self, points, epsilon, max_dist):
        self._slots = {}
        self._epsilon = epsilon
        self._points = points
        self._max_dist = max_dist

        self._dimension = points[0].get_dimension()
        self._size = int(2*math.ceil(1 / float(epsilon)))

        self.construct_slots()

    def construct_slots(self):
        for point in self._points:
            self.find_slot(point)

    def find_slot(self, point):
        chosen_slot = []
        for coord in point.get_point_arr():
            for index in xrange(-self._size/2, self._size/2):
                if index*self._epsilon*self._max_dist > coord:
                    chosen_slot.append((index-1)*self._epsilon*self._max_dist)
        self._slots[tuple(chosen_slot)] = point

    def get_coreset(self):
        return self._slots.values()


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
