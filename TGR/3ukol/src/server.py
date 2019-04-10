#!/usr/bin/env python3
from graphs import Graph
from nodes import Transformer


def run(data):
    servers = Graph(data, Transformer, " - ", ": ")
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
    for key in res:
        direction = res[key].pop()
        total += servers.vertex_cost(key, direction)
        out = out + " - " + direction

    print(out + ": " + str(total))
