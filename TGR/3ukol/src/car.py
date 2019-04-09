#!/usr/bin/env python3
from graphs import Graph
from nodes import Transformer
from parse import invert_dict


def run(data):
    start = "Vy"
    car = Graph(data, Transformer, " - ", ": ")
    endpoints = car.nodes.keys()

    res = {}
    for endpoint in endpoints:
        path, cost = car.dijkstra(start, endpoint)
        res[endpoint] = 0 - cost

    weights, inverted = invert_dict(res)
    for weight in reversed(weights):
        for endpoint in sorted(inverted[weight]):
            print(f"{endpoint}: {weight}")
