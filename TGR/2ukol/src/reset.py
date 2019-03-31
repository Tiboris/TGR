#!/usr/python3
from copy import deepcopy  # tmp
from graphs import Network
from nodes import Transformer


def cost(vertices):
    total_cost = 0
    for vertex, cost in vertices.items():
        total_cost += cost

    return total_cost


def run(data):
    transformers = Network(data, Transformer, " - ", ": ")
    transformers.print_graph()

    after_reset = deepcopy(transformers)

    print("Hodnoceni:", cost(after_reset.vertices))
