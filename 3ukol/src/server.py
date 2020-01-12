#!/usr/bin/env python3
from graphs import Graph
from nodes import Transformer


def run(data):
    servers = Graph(data, Transformer, " - ", ": ", oriented=True)
    res = {}
    out = ""

    for node in servers.nodes:
        if not out:
            out = node
        best = float("inf")
        for neighbour in servers.nodes[node].neighbours():
            if neighbour in res.keys():
                continue

            path, cost = servers.dijkstra(node, neighbour)
            if cost < best:
                best = cost
                res[node] = path

    total = 0
    to_unpack = len(res)

    while to_unpack:
        key = out[-1]
        direction = res[key].pop()
        total += servers.vertex_cost(key, direction)
        out = out + " - " + direction
        to_unpack -= 1

    print(out + ": " + str(total))
