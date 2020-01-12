#!/usr/python3
from graphs import AVLTree


def run(data):
    tree = AVLTree()
    for number in data:
        tree.insert(int(number))
        tree.print_level_order()
