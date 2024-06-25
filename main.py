from functions import *
import time


# retrieve all settlements and metrocities
def load_data(filename):
    global metro
    global settlements
    data = pandas.read_csv(filename, delimiter='\t', engine='python')
    settlements = data[data.iloc[:, 7] == 'ADM3']
    metro = settlements[settlements.iloc[:, 14] >= 300000]
    settlements = settlements.drop(metro.index)


def main():
    start_time = time.time()
    global metro
    global settlements
    load_data("PL.txt")

    # max_value = 100
    settlements_to_metros = {}
    interation_number = 1
    # max_value >= 0.2465969639416065 and

    while len(settlements) != 0:

        before_settlements = len(settlements)
        before_settlements_to_metros = len(settlements_to_metros)

        # calculate all radius of all metrocities
        radius_metro = {}
        for index, city in metro.iterrows():
            city_name = city.iloc[2]
            population = city.iloc[14]
            radius_metro[city_name] = radius(population)

        # calculate impact of each settlement for each metrocity
        arr = []
        for index, settlement in settlements.iterrows():
            subarr = []
            for indext, city in metro.iterrows():
                settlement_lat = settlement.iloc[4]
                settlement_lon = settlement.iloc[5]
                metro_lat = city.iloc[4]
                metro_lon = city.iloc[5]
                distance = calculate_distance(settlement_lat, settlement_lon, metro_lat, metro_lon)
                curr_metro_radius = radius_metro[city.iloc[2]]
                impact = calcualate_metrocity_impact(curr_metro_radius, distance)
                subarr.append(impact)
            arr.append(subarr)

        # find n most impacted settlements
        number_of_indexes = 200
        indexes = find_n_smallest_indexes_2d(arr, number_of_indexes)
        indexes = sorted(indexes)

        # try to merge n most impacted settlements with metrocities
        for i in indexes[:]:
            row_index = i[0]
            # ensure that the settlement wasn't already added this iteration
            if (str(settlements.iloc[row_index, 2]) + " " + str(settlements.iloc[row_index, 4]) + " " + str(
                    settlements.iloc[row_index, 5])) in settlements_to_metros:
                indexes.remove(i)
            else:
                col_index = i[1]
                settlements_to_metros[(
                            str(settlements.iloc[row_index, 2]) + " " + str(settlements.iloc[row_index, 4]) + " " + str(
                        settlements.iloc[row_index, 5]))] = metro.iloc[col_index, 2]
                metro.iloc[col_index, 14] += settlements.iloc[row_index, 14]

        # remove n most impacted settlements already merged
        #if (len(settlements) > number_of_indexes):
        for i in reversed(indexes):
            row_index = i[0]
            settlements.drop(index=settlements.index[row_index], inplace=True)
        #else:
        #    settlements = {}

        print("Iteration nr. " + str(interation_number))
        print("Current hashmap len: " + str(len(settlements_to_metros)) + " added: " + str(len(settlements_to_metros)-before_settlements_to_metros))
        print("Current settlements len: " + str(len(settlements)) + " removed: " + str(before_settlements-len(settlements)))
        interation_number += 1

    # print results
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Finish")
    print(f"Elapsed time: {elapsed_time} seconds")
    print("Current hashmap len: " + str(len(settlements_to_metros)) + " Amount of metrocities: " + str(len(metro)))
    print(settlements_to_metros)
    #print(settlements)


if __name__ == "__main__":
    main()
