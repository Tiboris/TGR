#!/usr/python3
from re import search

import parse


def run(data):
    crossroads = parse.crossroads(data)
    print(crossroads)
    for crossroad, neighbours in crossroads.items():
        for neighbour in neighbours:
            res = search(r"(\w)\((-?\d)\)", neighbour)
            print(crossroad, "-", res.group(1), "cost", res.group(2))
