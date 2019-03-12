#!/usr/python3
from nodes import Person
from collections import OrderedDict
import parse


def print_dict(dictionary):
    for key in dictionary:
        print(str(key) + ": " + str(dictionary[key]))


def get_people_data(data):
    nodes = []
    people = {}

    nodes = parse.nodes(data, nodes)
    for name in nodes:
        people[name] = Person(name)

    parse.connections(data, people, " - ")
    return people


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
    for person in sort_by_degree(people):
        print(person + " (%s)" % people[person].conn_cnt())


def format_out(chart):
    output = ""
    for position in chart:
        line = ""
        for name in chart[position]:
            if line:
                separator = ", "
            else:
                separator = line

            line = line + separator + name

        output = output + line + " (" + str(position) + ")\n"
    return output


def get_influencers(influencers, best, influencers_cnt=3, cost=0):
    if influencers_cnt == 0:
        return cost

    print_dict(influencers)
    print_dict(best)

    for person in influencers:
        value = best[influencers[person].conn_cnt()]
        best[influencers[person].conn_cnt()] = add_list_item(value, person)


def subtask2(people):
    influencers = sort_by_degree(people)
    chart = invert_dict(influencers)
    best = OrderedDict()
    for index in range(max(chart, key=int), -1, -1):
        best[index] = []

    print_dict(best)

    get_influencers(influencers, best)
    print(format_out(best))


def run(data):
    people = get_people_data(data)
    print("Task 1:")
    subtask1(people)
    print("\nTask 2:")
    subtask2(people)
