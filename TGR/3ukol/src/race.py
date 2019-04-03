#!/usr/python3
import parse


def run(data):
    crossroad, neigbours = parse.crossroads(data)
    print(crossroad, neigbours)
