#!/usr/python3
from graphs import Graph
from nodes import Town
import parse


def print_routes(routes):
    for town, route in routes.items():
        print(town + " -> " + route.direction())


def fuse(lower_towns, upper_towns):
    fused = {}
    redundant = {}

    for town, route in upper_towns.items():
        if town.lower() in lower_towns and \
            lower_towns[town.lower()].has_connection_with(
                route.direction().lower()):
            redundant[town.lower()] = lower_towns[town.lower()]

    fused = {**upper_towns, **lower_towns}
    for key in redundant:
        del fused[key]

    return fused, redundant


def run(data):
    data_lower = []
    data_upper = []
    for line in data:
        if line[0].istitle():
            data_upper.append(line)
        else:
            data_lower.append(line)

    lower_towns = Graph(data_lower, Town, " -> ")
    upper_towns = Graph(data_upper, Town, " -> ")

    new_routes, to_delete = fuse(lower_towns.nodes, upper_towns.nodes)

    print_routes(new_routes)
    print("----")
    print_routes(to_delete)
