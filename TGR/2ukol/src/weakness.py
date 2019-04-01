#!/usr/python3
from copy import deepcopy
from graphs import Network
from nodes import Transformer


def subtask1(transformers):
    res = []
    for vertex in transformers.vertices:
        tmp = deepcopy(transformers)
        tmp.remove_vertex(vertex)
        if tmp.is_multi_component():
            res.append(vertex)

    return res


def subtask2(transformers):  # node removal
    res = []
    for node in transformers.nodes:
        tmp = deepcopy(transformers)
        tmp.remove_node(node)
        if tmp.is_multi_component():
            res.append(node)

    return res


def run(data):
    transformers = Network(data, Transformer, " - ", ": ")
    if not transformers.is_multi_component():
        print("\n".join([v for v in subtask1(transformers)]))
        print("\n".join([v for v in subtask2(transformers)]))
    else:
        print("Error: Input has more than one component")
