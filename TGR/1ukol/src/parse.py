#!/usr/python3
def nodes(data, nodes):
    for node in data[0].split(','):
        nodes.append(node.split()[0])

    del data[0]
    return nodes


def connections(data, nodes, delimiter):
    for connetion in data:
        a, b = connetion.split(delimiter)
        if a in nodes and b in nodes:
            nodes[a].connect(b)
            if ">" not in delimiter:
                nodes[b].connect(a)


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
