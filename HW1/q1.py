
import random


# point utilities

# Returns the euclidian distance between two points
def euclid_dist(point1, point2):
    dist = 0
    for coord_index in range(len(point1)):
        dist += (point1[coord_index] - point2[coord_index])**2
    return dist

def farther_point(source_point, point1, point2):
    if (
        euclid_dist(source_point, point1)
        > euclid_dist(source_point, point2)
    ):
        return point1
    return point2

def furthest_point(source_point, points):
    return reduce(
        (
            lambda point1, point2 : point1 if (
                euclid_dist(source_point, point1)
                > euclid_dist(source_point, point2)
            ) else point2
        ),
        points
    )

# Main function
def one_center_grid_coreset(points, epsilon):
    # choose the first point as u
    chosen_point = points[0]
    print furthest_point(chosen_point, points)


def main():
    input_points = [
        [0,0,0,0],
        [1,1,1,1],
        [2,2,2,2],
    ]
    epsilon = 1

    # test function
    one_center_grid_coreset(input_points, epsilon)




if __name__ == "__main__":
    main()
