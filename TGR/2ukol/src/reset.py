#!/usr/python3
from copy import deepcopy
from graphs import Network
from nodes import Transformer
from parse import invert_dict

DELIM = " - "


def run(data):
    transformers = Network(data, Transformer, DELIM, ": ")

    after_reset = deepcopy(transformers)  # copy object
    after_reset.empty()  # empty it

    weights, inverted = invert_dict(transformers.vertices)

    to_cover = set(transformers.nodes.keys())
    covered = set()

    while covered != to_cover:
        for weight in weights:
            for vertex in inverted[weight]:
                a, b = vertex.split(DELIM)
                new = deepcopy(after_reset)

                # connect nodes in graph
                new.nodes[a].connect(b)
                new.nodes[b].connect(a)
                # add vertice to vertices
                new.vertices[vertex] = weight

                if not new.has_loop():
                    after_reset = new
                    covered.add(a)
                    covered.add(b)

    total_cost = 0
    for vertex, cost in after_reset.vertices.items():
        print('{}: {}'.format(vertex, cost))
        total_cost += cost

    print("Hodnoceni:", total_cost)
