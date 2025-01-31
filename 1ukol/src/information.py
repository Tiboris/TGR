#!/usr/python3
from collections import OrderedDict
from copy import deepcopy

from graphs import Graph
from nodes import Person


def add_list_item(record, item):
    if record is None:
        record = []

    record.append(item)
    return record


def invert_dict(nodes):
    nodes_by_degree = {}
    for key in nodes:
        try:
            record = nodes_by_degree[nodes[key].conn_cnt()]
        except KeyError:
            record = []
        nodes_by_degree[nodes[key].conn_cnt()] = add_list_item(record, key)

    return nodes_by_degree


def sort_by_degree(nodes):
    sorted_nodes = OrderedDict()
    nodes_by_degree = invert_dict(nodes)

    for degree in range(max(nodes_by_degree, key=int), 0, -1):
        for node in nodes_by_degree[degree]:
            sorted_nodes[node] = nodes[node]

    return sorted_nodes


def subtask1(people):
    for person in sort_by_degree(people.nodes):
        print(person + " (%s)" % people.nodes[person].conn_cnt())


def format_out(chart, best):
    output = ""
    for position in chart:
        if position == 0:
            continue
        line = ""
        for name in chart[position]:
            if name not in best:
                continue

            if line:
                separator = ", "
            else:
                separator = ""

            line = line + separator + name

        if not line:
            continue

        if output:
            line = "\n" + line

        if line:
            output = output + line + " (" + str(position) + ")"

    return output


def get_best_influencer(influencers):
    best = {}
    sheeps = []
    for name, person in influencers.items():
        sheeps.append(name)
        for connection in person.connections:
            sheeps.append(connection)
            for sheep in influencers[connection].connections:
                if sheep not in sheeps:
                    sheeps.append(sheep)

        best[name] = len(sheeps)
        sheeps = []

    best = sorted(best, key=best.get, reverse=True)
    return best[:3]


def subtask2(people):
    influencers = sort_by_degree(people.nodes)
    chart = invert_dict(influencers)
    best = get_best_influencer(deepcopy(influencers))
    print(format_out(chart, best))


def run(data):
    people = Graph(data, Person, " - ")
    print("Task 1:")
    subtask1(people)
    print("\nTask 2:")
    subtask2(people)
