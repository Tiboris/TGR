#!/usr/python3
import parse
from nodes import Component


def get_compounds(data):
    graph1 = []
    graph1 = parse.nodes(data, graph1)
    graph2 = []
    graph2 = parse.nodes(data, graph2)

    compound1 = {}
    for element in parse.compound_elements(graph1):
        compound1[element] = Component(element)

    parse.connections(graph1, compound1, '-')

    compound2 = {}
    for element in parse.compound_elements(graph2):
        compound2[element] = Component(element)

    parse.connections(graph2, compound2, '-')

    return compound1, compound2


def subtask0(compound1, compound2):
    return str(len(compound1) == len(compound2)).lower()


def subtask1(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask2(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask3(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask4(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask5(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask6(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask7(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask8(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def subtask9(compound1, compound2):
    return str(len(compound1) != len(compound2)).lower()


def run(data):
    compound1, compound2 = get_compounds(data)
    parse.print_graph(compound1)
    parse.print_graph(compound2)
    print("* |U1| = |U2|: " + subtask0(compound1, compound2))
    print("* |H1| = |H2|: " + subtask2(compound1, compound2))
    print("* Jsou-li u, v sousední uzly, pak i (u), (v) jsou sousední uzly: " +
          subtask2(compound1, compound2))
    print("* Grafy mají stejnou posloupnost stupňů uzlů: " +
          subtask3(compound1, compound2))
    print("* Pak pro každý uzel v z U platí")
    print("\t– stupeň uzlu v je roven stupni uzlu φ(v): " +
          subtask4(compound1, compound2))
    print("\t– množina stupňů sousedů uzlu v je rovna množině stupňů "
          "sousedů uzlu φ(v): " + subtask5(compound1, compound2))
    print("* Pak pro každý sled platí")
    print("\t– obraz sledu je opět sled: " + subtask6(compound1, compound2))
    print("\t– obraz tahu je opět tah: " + subtask7(compound1, compound2))
    print("\t– obraz cesty je opět cesta: " + subtask8(compound1, compound2))
    print("\t– délka sledu zůstává zachována: " +
          subtask9(compound1, compound2))
