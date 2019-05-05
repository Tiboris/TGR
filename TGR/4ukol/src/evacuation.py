#!/usr/bin/env python3
from graphs import Flow


def run(data):
    flow = Flow(data, exit_node="EXIT")

    flow.edmons_karp()

    print("Group size:", flow.group_size)
    for door in flow.doors:
        vertex = flow.vertices[flow.doors[door]]
        if vertex.flow == vertex.capacity:
            opt_flow = "]{}[".format(vertex.flow)
        else:
            opt_flow = vertex.flow
        print(door + ":", opt_flow)
