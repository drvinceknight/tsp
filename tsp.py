"""
A library with functionality for solving the travelling sales agent problem.
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_tour(x, y, tour):
    """
    Given a tour, and a set of coordinates x, y, it plots the tour.
    """
    ordered_x = x[tour]
    ordered_y = y[tour]
    plt.figure()
    plt.scatter(x, y)
    plt.plot(ordered_x, ordered_y)


def get_tour(number_of_stops, seed=None):
    """
    Given a number of stops, it creates a tour.

    If a seed is passed then it creates a random tour.

    This is done by selecting number from 1 -> number of_stops (exclusive)
    and adding 0 to the start and end.
    """
    internal_stops = list(range(1, number_of_stops))
    if seed is not None:
        np.random.seed(seed)
        np.random.shuffle(internal_stops)
    return [0] + internal_stops + [0]


def swap_stops(tour, steps):
    """
    This swaps two stops in a tour, the two stops are given by `steps`.
    """
    i, j = sorted(steps)
    new_tour = tour[:i] + tour[i : j + 1][::-1] + tour[j + 1 :]
    return new_tour


def get_cost(tour, distance_matrix):
    """
    Returns the cost of a tour.

    This picks out elements of the distance matrix given by
    successive stops.

    For example, if 4,5 is part of the tour. We go from 4 to 5 then
    that contributes distance_matrix[4, 5] to the overall cost.
    """
    return sum(
        distance_matrix[current_stop, next_stop]
        for current_stop, next_stop in zip(tour[:-1], tour[1:])
    )


def run_2_opt_algorithm(
    number_of_stops,
    distance_matrix,
    iterations,
    seed=None,
):
    """
    Runs the 2-opt algorithm (wiki link: https://en.wikipedia.org/wiki/2-opt).
    """
    tour = get_tour(number_of_stops=number_of_stops, seed=seed)
    best_cost = get_cost(tour=tour, distance_matrix=distance_matrix)
    for _ in range(iterations):
        two_indices = np.random.choice(range(1, number_of_stops), 2)
        candidate_tour = swap_stops(tour=tour, steps=two_indices)
        if (
            cost := get_cost(tour=candidate_tour, distance_matrix=distance_matrix)
        ) <= best_cost:
            best_cost = cost
            tour = candidate_tour
    return tour


def add(a, b):
    return a + b
