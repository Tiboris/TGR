#!/usr/python3
from graphs import Graph
from nodes import Transformer


def run(data):
    components = Graph(data, Transformer, " - ", ": ")
    components.print_graph()
