#!/usr/python3
def nodes(data):
    nodes = []
    for node in data[0].split(','):
        nodes.append(node.split()[0])

    del data[0]
    return nodes


def transformers(data, delimiter=" - ", weight_delim=": "):
    nodes = []
    for line in data:
        conn, _ = line.split(weight_delim)
        a, b = conn.split(delimiter)
        if a not in nodes:
            nodes.append(a)

        if b not in nodes:
            nodes.append(b)

    return nodes


def connections(data, nodes, delimiter, weight_delim=""):

    vertices = {}
    for line in data:
        conn, weight = line.split(weight_delim)
        a, b = conn.split(delimiter)
        if a in nodes and b in nodes:
            vertices[conn] = int(weight) if weight else 0
            nodes[a].connect(b)
            if ">" not in delimiter:
                nodes[b].connect(a)

    return vertices


def compound_elements(graph):
    elements = []
    for connection in graph:
        a, b = connection.split('-')
        if a not in elements:
            elements.append(a)

        if b not in elements:
            elements.append(b)

    return elements


def print_graph(dictionary):
    print("Graph ===================")
    for key in dictionary:
        print(str(key) + ": " + str(dictionary[key].connections))
    print("=========================")
