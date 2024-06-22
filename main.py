from functions import *

def load_data(filename):
    global metro
    global settlements
    data = pandas.read_csv(filename, delimiter='\t', engine='python')
    settlements = data[data.iloc[:, 7] == 'ADM3']
    metro = settlements[settlements.iloc[:, 14] >= 200000]
    settlements = settlements.drop(metro.index)


def main():
    print("Hello, world!")
    load_data("PL.txt")
    print(metro.iloc[:, [2, 6, 7, 14]])

    radius_metro = {}

    for index, city in metro.iterrows():
        city_name = city.iloc[2]
        population = city.iloc[14]
        radius_metro[city_name] = radius(population)

    print(radius_metro)

if __name__ == "__main__":
    main()









