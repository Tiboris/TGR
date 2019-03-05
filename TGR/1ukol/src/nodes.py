#!/usr/python3
class Node:
    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.connections = []

    def has_connection_with(self, node_name):
        return node_name in self.connections

    def connect(self, node_name):
        if not self.has_connection_with(node_name):
            self.connections.append(node_name)


class Person(Node):
    def __init__(self, name):
        self.name = self.nodeid = name
        self.connections = []


class Town(Person):
    pass


class Component(Node):
    # H = 1  # Vodík s jednou vazbou
    # O = 2  # Kyslík se dvěma vazbami
    # B = 3  # Bor se třemi
    # C = 4  # Uhlík se čtyřmi
    # N = 5  # Dusík s pěti
    # S = 6  # Síra se šesti
    def __init__(self, kind):
        self.kind = self.nodeid = kind
        self.connections = []

    def connect(self, node_name):
        self.kind[0]
        if not self.has_connection_with(node_name):
            self.connections.append(node_name)
