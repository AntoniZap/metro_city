from functions import *

def load_data(filename):
    global metro
    global settlements
    data = pandas.read_csv(filename, delimiter='\t', engine='python')
    settlements = data[data.iloc[:, 7] == 'ADM3']
    metro = settlements[settlements.iloc[:, 14] >= 200000]
    settlements = settlements.drop(metro.index)


def main():
    global metro
    global settlements
    load_data("PL.txt")

    radius_metro = {}

    for index, city in metro.iterrows():
        city_name = city.iloc[2]
        population = city.iloc[14]
        radius_metro[city_name] = radius(population)
    cities_to_metros = {}

    for index, settlement in settlements.iterrows():
        for indext, city in metro.iterrows():

            settlement_lat = settlement.iloc[4]
            settlement_lon = settlement.iloc[5]
            metro_name = city.iloc[2]
            metro_lat = city.iloc[4]
            metro_lon = city.iloc[5]
            distance = calculate_distance(settlement_lat, settlement_lon,metro_lat, metro_lon)

            if distance < radius_metro[metro_name]:

                settlement_name = settlement.iloc[2]
                cities_to_metros[settlement_name] = metro_name


    print(cities_to_metros)
    print(len(cities_to_metros))

    print(calcualate_metrocity_impact(100, 1))
    print(calcualate_metrocity_impact(100, 20))


if __name__ == "__main__":
    main()









