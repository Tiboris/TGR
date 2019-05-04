#!/usr/bin/env python3
from graphs import Flow


def run(data):
    flow = Flow(data, exit_node="EXIT")
    flow.print_graph()
