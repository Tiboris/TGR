#!/usr/python3
from graphs import Graph
from nodes import Transformer


def run(data):
    transformers = Graph(data, Transformer, " - ", ": ")
    transformers.print_graph()

    for vertex in transformers.vertices:
        print (vertex, transformers.vertices[vertex])
