#!/usr/bin/env python3
from graphs import City


def run(data):
    city = City(data)
    # print(city)
    city.print_map()
    print("-------\nOutput:")
    key_of_one_minimal = min(city.costs, key=city.costs.get)
    for mapping in city.combinations[key_of_one_minimal]:
        print(
            mapping[0], mapping[1],
            city.distance[mapping[0][:3] + "-" + mapping[1][:3]]
        )

    print("Celkem:", city.costs[key_of_one_minimal])
