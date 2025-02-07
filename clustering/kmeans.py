from collections import defaultdict
from math import inf
import random
import csv
import numpy as np


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    center = []
    if len(points) < 1:
        return None
    else:
        for i in range(len(points[0])):
            sum = 0
            for j in range(len(points)):
                sum += points[j][i]
            center.append(sum / len(points))
        return center
    # raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    centers = []
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, data_set):
        clustering[assignment].append(point)
    for key, value in clustering.items():
        centers.append(point_avg(value))

    return centers
    # raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return np.sqrt(np.sum(np.square(np.array(a) - np.array(b))))
    # raise NotImplementedError()


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(data_set, k)
    # raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):
    list =[]
    with open(dataset_file) as file:
        reader = csv.reader(file)
        for point in reader:
            pointdata = []
            for cod in point:
                pointdata.append(int(cod))
            list.append(pointdata)
    return list
    # raise NotImplementedError()


def cost_function(clustering):
    cost = 0
    for key in clustering.keys():
        values = clustering[key]
        center = point_avg(values)
        for value in values:
            cost += distance(center, value)
    return cost
    # raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering
