#!/usr/python3
from copy import deepcopy
from graphs import Graph
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
    transformers = Graph(data, Transformer, " - ", ": ")
    subtask1(transformers)
    print("-|-|-|-|-|-|-|-|-|-")
    subtask2(transformers)
