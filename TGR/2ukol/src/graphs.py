#!/usr/python3
import nodes
import parse
from structures import Stack, Queue
from collections import OrderedDict


class Graph():
    def __init__(self, data, Instance, delimiter, weight_delim=""):
        if Instance == nodes.Component:
            data = parse.nodes(data)
            input_nodes = parse.compound_elements(data)
        elif Instance == nodes.Transformer:
            input_nodes = parse.transformers(data)
        else:
            input_nodes = parse.nodes(data)

        self.nodes = OrderedDict()
        for key in input_nodes:
            self.nodes[key] = Instance(key)

        self.vertices = parse.connections(data, self.nodes,
                                          delimiter, weight_delim)

    def print_graph(self):
        print("Graph ===================")
        for key in self.nodes:
            print(str(key) + ": " + str(self.nodes[key].connections))
        print("=========================")

    def nodes_cnt(self):
        return len(self.nodes)

    def vertex_cnt(self):
        return len(self.vertices)

    def vertex_cost(self, a, b):
        for vertex, cost in self.vertices.values():
            if a in vertex and b in vertex:
                return cost

        return 0  # returns 0 if given node names are not in graph

    def disconnect(self, a, b):
        self.nodes[a].disconnect(b)
        self.nodes[b].disconnect(a)
        try:
            self.vertices.remove(tuple([a, b]))
        except ValueError:
            pass

    def find_path(self, start, end, path=[]):
        """
        Inspired from: https://www.python.org/doc/essays/graphs/
        """
        if start not in self.nodes or end not in self.nodes:
            return None

        path = path + [start]
        if start == end:
            return path

        for node in self.nodes[start].connections:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath

        return None

    def find_shortest_path(self, start, end, path=[]):
        """
        Inspired from: https://www.python.org/doc/essays/graphs/
        """
        if start not in self.nodes or end not in self.nodes:
            return None

        path = path + [start]
        if start == end:
            return path

        shortest = None
        for node in self.nodes[start].connections:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest

    def find_all_paths(self, start, end, path=[]):
        """
        Inspired from: https://www.python.org/doc/essays/graphs/
        """
        if start not in self.nodes or end not in self.nodes:
            return []

        path = path + [start]
        if start == end:
            return [path]

        paths = []
        for node in self.nodes[start].connections:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths


class Network(Graph):
    def unmark(self):
        for node in self.nodes:
            self.nodes[node].mark = False

    def has_loop(self):
        # pre každý transformátor nájdem všetky možné cesty k ostatným
        # ak má jeden transformátor viac ako jednu cestu k nejakému z topológie
        # topológia má slučky a nastavím si loop_in_topo na True.

        loop_in_topo = False
        for start in self.nodes:
            for end in self.nodes:
                if end != start:
                    paths = self.find_all_paths(start, end)
                    if len(paths) > 1:
                        loop_in_topo = True
                        break
            if loop_in_topo:
                break

        return loop_in_topo
