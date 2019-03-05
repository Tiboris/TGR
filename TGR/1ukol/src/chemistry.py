#!/usr/python3
import parse


def run(data):
    compound1 = []
    compound1 = parse.nodes(data, compound1)
    compound2 = []
    compound2 = parse.nodes(data, compound2)
    print(compound1)
    print(compound2)
