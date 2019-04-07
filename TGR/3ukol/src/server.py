#!/usr/python3
from graphs import Graph
from nodes import Transformer


def run(data):
    servers = Graph(data, Transformer, " - ", ": ")
    servers.print_graph()
