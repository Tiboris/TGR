#!/usr/python3
import parse
from nodes import Node


def run(data):
    towns = {}
    nodes = []
    nodes = parse.nodes(data, nodes)
    nodes = parse.nodes(data, nodes)
    for name in nodes:
        towns[name] = Node(name)

    parse.connections(data, towns, " -> ")
    print(data)
    for person in towns:
        print(person + " -> " + str(towns[person].connections))
