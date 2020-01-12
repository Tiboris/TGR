#!/usr/bin/env python3
def nodes(data):
    nodes = []
    for node in data[0].split(","):
        nodes.append(node.split()[0])

    del data[0]
    return nodes


def transformers(data, delimiter=" - ", weight_delim=": ", oriented=False):
    nodes = []
    for line in data:
        conn, _ = line.split(weight_delim)
        a, b = conn.split(delimiter)
        if a not in nodes:
            nodes.append(a)

        if not oriented and b not in nodes:
            nodes.append(b)

    return nodes


def crossroads(data, delimiter=": ", record_delim=","):
    res = {}
    for line in data:
        crossroad, records = line.split(delimiter, maxsplit=1)
        neigbours = [r.strip() for r in records.split(record_delim)]
        res[crossroad] = neigbours

    return res


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
        a, b = connection.split("-")
        if a not in elements:
            elements.append(a)

        if b not in elements:
            elements.append(b)

    return elements


def add_list_item(record, item):
    if record is None:
        record = []

    record.append(item)
    return record


def invert_dict(nodes):
    inverted_dict = {}
    for key in nodes:
        try:
            record = inverted_dict[nodes[key]]
        except KeyError:
            record = []
        inverted_dict[nodes[key]] = add_list_item(record, key)

    return inverted_dict


def print_graph(dictionary):
    print("Graph ===================")
    for key in dictionary:
        print(str(key) + ": " + str(dictionary[key].connections))
    print("=========================")
