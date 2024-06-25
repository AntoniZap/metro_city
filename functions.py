import math
import numpy as np
import pandas
import heapq

def radius(population):
    METRO_CITY_POPULATION_CONSTANT = -1 / 1443000
    MIN_METRO_CITY_RADIUS = 10
    MAX_METRO_CITY_RADIUS = 100 - MIN_METRO_CITY_RADIUS
    return MIN_METRO_CITY_RADIUS + MAX_METRO_CITY_RADIUS * (1 - np.exp(METRO_CITY_POPULATION_CONSTANT * population))

def calcualate_metrocity_impact(max_radius, distance_to_metro_city):
    METRO_CITY_POWER_CONSTANT = -1.4
    impact = np.exp(METRO_CITY_POWER_CONSTANT * distance_to_metro_city / max_radius)
    return impact

def calculate_distance(point_a_lat, point_a_lon, point_b_lat, point_b_lon):
    lat1 = math.radians(point_a_lat)
    lon1 = math.radians(point_a_lon)
    lat2 = math.radians(point_b_lat)
    lon2 = math.radians(point_b_lon)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = 6371 * c
    return distance

def find_n_smallest_indexes_2d(matrix, n):
    flattened = [(matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    smallest_with_indexes = heapq.nlargest(n, flattened)
    smallest_indexes = [(row, col) for value, row, col in smallest_with_indexes]
    return smallest_indexes

def first_digit_of_tuple(t):
    return int(str(t[0])[0])