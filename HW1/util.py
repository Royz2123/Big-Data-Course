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
