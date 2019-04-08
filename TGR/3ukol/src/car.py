#!/usr/bin/env python3
from graphs import Graph
from nodes import Transformer
from parse import invert_dict


def run(data):
    start = "Vy"
    car = Graph(data, Transformer, " - ", ": ")
    endpoints = car.nodes.keys()

    dic = {}
    for endpoint in endpoints:
        cost = len(car.find_shortest_path(start, endpoint))
        # TODO ^^^ cost, path = djixtra(start, endpoint)
        dic[endpoint] = 0 - cost

    weights, inverted = invert_dict(dic)
    for weight in reversed(weights):
        for endpoint in sorted(inverted[weight]):
            print(f"{endpoint}: {weight}")
