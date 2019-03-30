#!/usr/python3
from graphs import Network
from nodes import Transformer
from structures import Stack

conn_delim = " - "
weight_delim = ": "


def transformers_status_ok(transformers):
    for start in transformers.nodes:
        for end in transformers.nodes:
            if end != start:
                path = transformers.find_all_paths(start, end)
                print(path)

    transformers.unmark()
    transformers.print_graph()
    s = Stack()

    for vertex in transformers.vertices:
        s.push(vertex)
        s.print_content()

    return True


def run(data):
    transformers = Network(data, Transformer, conn_delim, weight_delim)

    if transformers_status_ok(transformers):
        print("Stav site OK")
    else:
        print("Stav site ERROR")
