from functions import *

def load_data(filename):
    global metro
    global settlements
    data = pandas.read_csv(filename, delimiter='\t', engine='python')
    settlements = data[data.iloc[:, 7] == 'ADM3']
    metro = settlements[settlements.iloc[:, 14] >= 350000]
    settlements = settlements.drop(metro.index)

def main():
    global metro
    global settlements
    load_data("PL.txt")


    max_value = 100
    settlements_to_metros = {}

    while max_value >= 0.2465969639416065:

        radius_metro = {}
        for index, city in metro.iterrows():
            city_name = city.iloc[2]
            population = city.iloc[14]
            radius_metro[city_name] = radius(population)

        arr = []
        for index, settlement in settlements.iterrows():
            subarr = []
            for indext, city in metro.iterrows():
                settlement_lat = settlement.iloc[4]
                settlement_lon = settlement.iloc[5]
                metro_lat = city.iloc[4]
                metro_lon = city.iloc[5]
                distance = calculate_distance(settlement_lat, settlement_lon,metro_lat, metro_lon)
                curr_metro_radius = radius_metro[city.iloc[2]]
                impact = calcualate_metrocity_impact(curr_metro_radius, distance)
                subarr.append(impact)
            arr.append(subarr)


        max_value = 0
        row_index = 0
        col_index = 0
        for i, row in enumerate(arr):
            for j, element in enumerate(row):
                if element > max_value:
                    row_index = i
                    col_index = j
                    max_value = element

        #indexes = find_n_smallest_indexes_2d(arr, 20)
        #print(f"The most impact this iteration is {max_value}")
        #print(settlements.iloc[row_index, 2])
        #print("is merged to")
        #print(metro.iloc[col_index, 2])

        settlements_to_metros[settlements.iloc[row_index, 2]] = metro.iloc[col_index, 2]
        #print(metro.iloc[col_index, 14])
        metro.iloc[col_index, 14] += settlements.iloc[row_index, 14]
        #print(metro.iloc[col_index, 14])
        settlements.drop(index= settlements.index[row_index], inplace=True)
        print(max_value)

    print(settlements_to_metros)

if __name__ == "__main__":
    main()









