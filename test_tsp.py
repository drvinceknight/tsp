import numpy as np
import matplotlib.pyplot as plt

import tsp

def test_get_tour_with_no_seed():
    number_of_stops = 4
    tour = tsp.get_tour(number_of_stops=number_of_stops)
    assert np.array_equal(tour, np.array([0, 1, 2, 3, 0]))


def test_get_tour_with_seed_1():
    number_of_stops = 4
    seed = 1
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    assert np.array_equal(tour, np.array([0, 1, 3, 2, 0])), f"Obtained output is {tour}"


def test_get_tour_with_seed_2():
    number_of_stops = 4
    seed = 2
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    assert np.array_equal(tour, np.array([0, 3, 2, 1, 0])), f"Obtained output is {tour}"

def test_swap_stops():
    tour = [0, 1, 3, 2, 4, 0]
    steps = (4, 1)
    new_tour = tsp.swap_stops(tour=tour, steps=steps)
    assert new_tour == [0, 4, 2, 3, 1, 0], f"Obtained output is {new_tour}"


def test_get_cost():
    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    tour = [0, 1, 2, 3, 0]
    cost = tsp.get_cost(tour=tour, distance_matrix=distance_matrix)
    assert cost == 24


def test_run_2_opt_algorithm_with_seed_0():
    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    number_of_stops = 4
    seed = 0
    iterations = 50
    tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
            distance_matrix=distance_matrix, seed=seed, iterations=iterations)
    assert tour == [0, 2, 3, 1, 0], f"Obtained output is {tour}"

def test_run_2_opt_algorithm_with_seed_1():
    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    number_of_stops = 4
    seed = 1
    iterations = 50
    tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
            distance_matrix=distance_matrix, seed=seed, iterations=iterations)
    assert tour == [0, 2, 1, 3, 0], f"Obtained output is {tour}"

def test_plot_tour():
    x = np.array([2, 3])
    y = np.array([2, 3])
    tour = np.array([0, 1, 0])
    plot = tsp.plot_tour(x=x, y=y, tour=tour)
    assert plot is None

def test_addition():
    a = 5
    b = 6
    assert tsp.add(a=a, b=b) == 11
