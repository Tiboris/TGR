#!/usr/python3
import parse
from nodes import Town


def print_routes(routes):
    for town, route in routes.items():
        print(town + " -> " + route.direction())


def fuse(upper_towns, lower_towns):
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
    lower_towns = {}
    upper_towns = {}
    nodes = []
    nodes = parse.nodes(data, nodes)

    for name in nodes:
        lower_towns[name] = Town(name)

    nodes = []
    nodes = parse.nodes(data, nodes)

    for name in nodes:
        upper_towns[name] = Town(name)

    parse.connections(data, lower_towns, " -> ")
    parse.connections(data, upper_towns, " -> ")

    new_routes, to_delete = fuse(lower_towns, upper_towns)

    print_routes(new_routes)
    print("----")
    print_routes(to_delete)
