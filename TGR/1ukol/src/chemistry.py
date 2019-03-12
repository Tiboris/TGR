#!/usr/python3
import parse
from nodes import Component


def get_compounds(data):
    graph1 = []
    graph1 = parse.nodes(data, graph1)
    graph2 = []
    graph2 = parse.nodes(data, graph2)

    compound1 = {}
    for element in parse.compound_elements(graph1):
        compound1[element] = Component(element)

    parse.connections(graph1, compound1, '-')

    compound2 = {}
    for element in parse.compound_elements(graph2):
        compound2[element] = Component(element)

    parse.connections(graph2, compound2, '-')

    return compound1, compound2


def run(data):
    compound1, compound2 = get_compounds(data)

    print(dict(compound1))
    print(dict(compound2))
