
import random


class Point(object):
    def __init__(self, point_arr):
        self._coords = map(float, point_arr)

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

# Main function
def one_center_grid_coreset(points, epsilon):
    # create point objects from input
    points = map(Point, points)

    # choose the first point as u
    chosen_point = points[0]
    print chosen_point.furthest_point(points)





def main():
    input_points = [
        [0,0,0,0],
        [1,1,1,1],
        [0,0,0,1.9],
    ]
    epsilon = 1

    # test function
    one_center_grid_coreset(input_points, epsilon)




if __name__ == "__main__":
    main()
