import numpy as np
import pandas

def load_data(filename):
    settlements = pandas.read_csv('PL.txt', delimiter='\t', engine='python')
    return settlements

def radius(population):
    METRO_CITY_POPULATION_CONSTANT = -1 / 1443000
    MIN_METRO_CITY_RADIUS = 10
    MAX_METRO_CITY_RADIUS = 100 - MIN_METRO_CITY_RADIUS
    return MIN_METRO_CITY_RADIUS + MAX_METRO_CITY_RADIUS * (1 - np.exp(METRO_CITY_POPULATION_CONSTANT * population))

def calcualate_metrocity_impact(max_radius, distance_to_metro_city):
    METRO_CITY_POWER_CONSTANT = -1.4
    impact = np.exp(METRO_CITY_POWER_CONSTANT * distance_to_metro_city / max_radius)
    return impact

data = load_data("PL.txt")
settlements = data[data.iloc[:, 7] == 'ADM3']

metro = settlements[settlements.iloc[:, 14] >= 200000]
#print(settlements.iloc[:, [2, 6, 7, 14]])
#print(metro.iloc[:, [2, 6, 7, 14]])

metro_entries = metro.index
settlements = settlements.drop(metro_entries)
#print(settlements.iloc[:, [2, 6, 7, 14]])







