#!/usr/bin/env python3
from graphs import Graph
from nodes import Crossroad
from parse import invert_dict


def run(data):
    crossroads = Graph(data, Crossroad)
    start = "A"
    distances, predecessors = crossroads.bellman_ford(start)
    successors = invert_dict(predecessors)
    path = start + " - " + successors[start][0]
    while (path.count(" - ") + 1) != len(crossroads.nodes):
        path = path + " - " + successors[path[-1]][0]

    bonuses = 0  # get all bonuses
    for node in crossroads.nodes:
        if crossroads.nodes[node].has_bonus:
            bonuses += path.count(node)

    print(path + ":", (-distances[path[-1]]) + bonuses)
