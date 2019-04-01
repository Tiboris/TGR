#!/usr/python3
class Node:
    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.connections = []

    def has_connection_with(self, node_id):
        return node_id in self.connections

    def connect(self, node_name):
        self.connections.append(node_name)

    def conn_cnt(self):
        return len(self.connections)

    def neighbours(self):
        return self.connections

    def disconnect(self, node_id):
        try:
            self.connections.remove(node_id)
        except ValueError:
            pass


class Person(Node):
    def __init__(self, name):
        self.name = self.nodeid = name
        self.connections = []

    def connect(self, node_name):
        if not self.has_connection_with(node_name):
            self.connections.append(node_name)


class Town(Person):
    def direction(self):
        return self.connections[0]


class Component(Node):  # DFS
    # H = 1  # Vodík s jednou vazbou
    # O = 2  # Kyslík se dvěma vazbami
    # B = 3  # Bor se třemi
    # C = 4  # Uhlík se čtyřmi
    # N = 5  # Dusík s pěti
    # S = 6  # Síra se šesti

    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.kind = self.nodeid[0]
        self.connections = []


class Transformer(Node):

    def __init__(self, nodeid):
        self.nodeid = self.name = nodeid
        self.mark = False
        self.connections = []

    def __iter__(self):
        return self

    def __repr__(self):
        return "<Transformer({})>".format(self.nodeid)


class Leaf():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.level = None

    def __repr__(self):
        return "<Node({})>".format(self.key)
