#!/usr/python3
def nodes(data, nodes):
    for node in data[0].split(', '):
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
