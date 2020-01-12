#!/usr/python3
from collections import OrderedDict

import nodes
import parse


class Graph:
    def __init__(self, data, Instance, delimiter):
        if Instance == nodes.Component:
            data = parse.nodes(data)
            input_nodes = parse.compound_elements(data)
        else:
            input_nodes = parse.nodes(data)

        self.nodes = OrderedDict()
        for key in input_nodes:
            self.nodes[key] = Instance(key)

        self.vertices = parse.connections(data, self.nodes, delimiter)

    def print_graph(self):
        print("Graph ===================")
        for key in self.nodes:
            print(str(key) + ": " + str(self.nodes[key].connections))
        print("=========================")

    def nodes_cnt(self):
        return len(self.nodes)

    def vertex_cnt(self):
        return len(self.vertices)

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
