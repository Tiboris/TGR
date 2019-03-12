#!/usr/python3
from nodes import Person
from collections import OrderedDict
import parse

NAME = 0


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


def get_influencer(influencers, connections):

    return True


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


def subtask2(people):
    best = []
    influencers_cnt = 3
    todo = [person for person in people]

    influencers = sort_by_degree(people)
    chart = invert_dict(influencers)

    best = {
        people[chart[max(chart, key=int)][NAME]].conn_cnt():
            chart[max(chart, key=int)][NAME]
        }

    print(todo)
    print(best)
    print(influencers.keys())
    print(format_out(best))
    print("MAGIC==============================")

    try:
        todo.remove(best[max(best, key=int)])
        influencer = influencers.pop(best[max(best, key=int)])
        for sheep in influencer.connections:
            todo.remove(sheep)
        influencers_cnt = influencers_cnt - 1
    except ValueError:
        if len(todo) == 0:
            return

    best[1] = "Adam"

    print(todo)
    print(best)
    print(influencers.keys())
    print(format_out(best))


def run(data):
    people = get_people_data(data)
    subtask1(people)
    subtask2(people)
