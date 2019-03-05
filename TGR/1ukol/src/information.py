#!/usr/python3
from nodes import Person
import parse


def run(data):
    nodes = []
    people = {}

    nodes = parse.nodes(data, nodes)
    for name in nodes:
        people[name] = Person(name)

    parse.connections(data, people, " - ")
    print (data)
    for person in people:
        print(person + " -> " + str(people[person].connections))
