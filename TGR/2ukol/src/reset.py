#!/usr/python3
from copy import deepcopy
from graphs import Network
from nodes import Transformer
from parse import invert_dict


def run(data):
    transformers = Network(data, Transformer, " - ", ": ")
    transformers.print_graph()

    after_reset = deepcopy(transformers)  # copy object
    after_reset.empty()
    after_reset.print_graph()
    print(after_reset.vertices)
    weights, inverted = invert_dict(transformers.vertices)

    for weight in weights:
        print(">> ", inverted[weight], weight)

    total_cost = 0
    for vertex, cost in after_reset.vertices.items():  # same invert and sort
        print(vertex, cost)
        total_cost += cost
    print("Hodnoceni:", total_cost)
