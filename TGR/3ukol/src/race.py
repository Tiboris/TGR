#!/usr/bin/env python3
from graphs import Graph
from nodes import Crossroad


def run(data):
    crossroads = Graph(data, Crossroad)
    crossroads.print_graph()
    for vertex, cost in crossroads.vertices.items():
        print(vertex, cost)

    for key, value in crossroads.nodes.items():
        print(value)
