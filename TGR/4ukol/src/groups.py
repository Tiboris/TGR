#!/usr/bin/env python3
from graphs import Graph
from nodes import Person


def run(data):
    people = Graph(data, Person, " - ")
    people.print_graph()
    groups = people.get_groups_a2()
    for group in groups:
        print(", ".join(g for g in group))
