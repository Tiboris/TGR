#!/usr/python3
import re
from collections import OrderedDict

import nodes
import parse
from structures import Queue
from structures import Stack


class Graph:
    def __init__(self, data, Instance, delimiter=",", weight_delim=""):
        self.delimiter = delimiter
        if Instance == nodes.Component:
            data = parse.nodes(data)
            input_nodes = parse.compound_elements(data)
        elif Instance == nodes.Transformer:
            input_nodes = parse.transformers(data)
        elif Instance == nodes.Crossroad:
            input_nodes = parse.crossroads(data)
        else:
            input_nodes = parse.nodes(data)

        self.nodes = OrderedDict()
        for key in input_nodes:
            if "+" in key:  # spartan race
                self.nodes[key[0]] = Instance(key[0], True)
            else:
                self.nodes[key] = Instance(key)

        if Instance == nodes.Crossroad:
            self.vertices = {}
            for crossroad, neighbours in input_nodes.items():
                for neighbour in neighbours:
                    res = re.search(r"(\w)\((-?\d+)\)", neighbour)
                    print(crossroad, "-", res.group(1), "cost", res.group(2))
                    self.vertices[
                        crossroad[0] + " - " + res.group(1)
                    ] = res.group(2)
                    self.nodes[crossroad[0]].connections.append(res.group(1))

        else:
            self.vertices = parse.connections(
                data, self.nodes, delimiter, weight_delim
            )

    def is_multi_component(self):
        paths = []
        for start in self.nodes:
            for end in self.nodes:  # paths without len
                paths.append(self.find_all_paths(start, end))
                if [] in paths:
                    return True

        return False

    def get_neighbours(self, objnode):
        res = []
        if isinstance(objnode, nodes.Transformer):
            for neighbour in objnode.connections:
                res.append(self.nodes[neighbour])
        else:
            for obj in objnode:
                for neighbour in obj.connections:
                    res.append(self.nodes[neighbour])

        return tuple(res)

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
            del self.vertices[a + self.delimiter + b]
        except KeyError:
            pass

    def remove_node(self, node_name):
        try:
            del self.nodes[node_name]
        except KeyError:
            pass

        to_del = []
        for vertex in self.vertices:
            if node_name in vertex:
                to_del.append(vertex)

        for vertex in to_del:
            del self.vertices[vertex]

        for node in self.nodes:
            if node_name in self.nodes[node].connections:
                self.nodes[node].connections.remove(node_name)

    def remove_vertex(self, vertex):
        a, b = vertex.split(self.delimiter)
        self.disconnect(a, b)

    def empty(self):
        self.vertices.clear()
        for key in self.nodes:
            self.nodes[key].connections = []

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

    def is_tree(self):
        return len(self.nodes) == (len(self.vertices) + 1)

    def bfs_walk(self):
        que = Queue()
        que.enqueue(next(iter(self.nodes.values())))
        while que.size() > 0:
            first = que.dequeue()
            if first.mark:
                continue
            else:
                print(first.name)
                first.mark = True

            for neighbour in first.connections:
                que.enqueue(self.nodes[neighbour])

    def dfs_walk(self):
        stack = Stack()
        stack.push(next(iter(self.nodes.values())))
        while stack.size() > 0:
            first = stack.pop()
            if first.mark:
                continue
            else:
                print(first.name)
                first.mark = True

            for neighbour in first.connections:
                stack.push(self.nodes[neighbour])

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


class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        return self.height if self.node else 0

    def insert(self, key):
        if self.node is None:
            self.node = nodes.Leaf(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            self.node.level = self.height
        elif key < self.node.key:
            self.node.left.insert(key)
        else:
            self.node.right.insert(key)

        self.update_heights(recursive=False)
        self.update_balances(recursive=False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def rotate_right(self):
        root = self.node
        left_child = self.node.left.node
        right_child = left_child.right.node

        self.node = left_child
        left_child.right.node = root
        root.left.node = right_child

    def rotate_left(self):
        root = self.node
        right_child = self.node.right.node
        left_child = right_child.left.node

        self.node = right_child
        right_child.left.node = root
        root.right.node = left_child

    def update_heights(self, recursive=True):
        if self.node is None:
            self.height = -1
        else:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = (
                max(self.node.left.height, self.node.right.height) + 1
            )
            self.node.level = self.height

    def update_balances(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def format_avl(self, tmp):
        res = ""
        for key, value in tmp.items():
            line = ""
            for record in value:
                line = line + record + ","

            res = res + line

        result = ""
        index = 0
        for char in res.split(","):
            index += 1
            if len(result) == 0 or index in [2 ** x - 1 for x in range(10)]:
                delim = "|"
            else:
                delim = ","

            if char:
                result += char + delim

        return result

    def print_level_order(self):
        q = Queue()
        tmp = OrderedDict()
        for index in range(self.get_height(), -2, -1):
            tmp[index] = []

        q.enqueue(self.node)
        level = 0

        while q.size() > 0:
            actual = q.dequeue()

            if actual:
                if level != actual.level:
                    level = actual.level

                tmp[level].append(str(actual.key))

                if actual.left:
                    q.enqueue(actual.left.node)

                if actual.right:
                    q.enqueue(actual.right.node)

                parent = actual

            else:
                if parent:
                    if parent.left.node or parent.right.node:
                        tmp[level - 1].append("_")
                    if not parent.left.node and not parent.right.node:
                        tmp[level - 1].append("_")

                    parent = actual
                else:
                    tmp[level - 1].append("_")

        result = self.format_avl(tmp)
        print(result)
