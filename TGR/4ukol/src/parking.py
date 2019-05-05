#!/usr/bin/env python3
from graphs import City


def run(data):
    city = City(data)
    print(city)
    city.print_map()
