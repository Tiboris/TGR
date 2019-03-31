#!/usr/python3
from copy import deepcopy
from graphs import Network
from nodes import Transformer


def subtask1(transformers):
    transformers.print_graph()
    print("-------------------")
    for vertex in transformers.vertices:
        tmp = deepcopy(transformers)
        tmp.remove_vertex(vertex)
        tmp.print_graph()


def subtask2(transformers):  # node removal
    transformers.print_graph()
    print("-------------------")
    for node in transformers.nodes:
        tmp = deepcopy(transformers)
        tmp.remove_node(node)
        tmp.print_graph()


def run(data):
    transformers = Network(data, Transformer, " - ", ": ")
    paths = []
    for start in transformers.nodes:
        for end in transformers.nodes:  # paths without len
            paths.append(transformers.find_all_paths(start, end))
            if [] in paths:
                print("NEDA SA MI")
            # paths.append()

    print(paths)

    
