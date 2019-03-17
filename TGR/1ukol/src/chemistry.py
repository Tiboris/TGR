#!/usr/python3
from graphs import Graph
from nodes import Component

COMPONENTS = {"H": 1,  # Vodík s jednou vazbou
              "O": 2,  # Kyslík se dvěma vazbami
              "B": 3,  # Bor se třemi
              "C": 4,  # Uhlík se čtyřmi
              "N": 5,  # Dusík s pěti
              "S": 6}  # Síra se šesti


def subtask0(compound1, compound2):
    """
    |U1| = |U2|
    """
    return compound1.nodes_cnt() == compound1.nodes_cnt()


def subtask1(compound1, compound2):
    """
    |H1| = |H2|
    """
    return compound1.vertex_cnt() == compound1.vertex_cnt()


def lookup_neighbours(compound1, compound2):
    neighbours = []  # FIXME
    return bool(neighbours)


def subtask2(compound1, compound2):
    """
    * Jsou-li u, v sousední uzly, pak i (u), (v) jsou sousední uzly
    """
    return subtask0(compound1, compound2) \
        and subtask1(compound1, compound2) \
        and lookup_neighbours(compound1, compound2)


def subtask3(compound1, compound2):
    """
    * Grafy mají stejnou posloupnost stupňů uzlů
    """
    c1 = sorted([len(value.connections) for value in compound1.nodes.values()])
    c2 = sorted([len(value.connections) for value in compound2.nodes.values()])
    return c1 == c2


def subtask4(compound1, compound2):
    """
    – stupeň uzlu v je roven stupni uzlu φ(v)
    """
    for element in COMPONENTS:
        cnt1 = [node for node in compound1.nodes if node == element]
        cnt2 = [node for node in compound2.nodes if node == element]
        if len(cnt1) != len(cnt2):
            return False

    return True


def subtask5(compound1, compound2):
    """
    – množina stupňů sousedů uzlu v je rovna množině stupňů
    """
    # FIXME
    return str(len(compound1) != len(compound2)).lower()


def subtask6(compound1, compound2):
    """
    – obraz sledu je opět sled
    """
    # FIXME
    return str(len(compound1) != len(compound2)).lower()


def subtask7(compound1, compound2):
    """
    – obraz tahu je opět tah
    """
    return str(len(compound1) != len(compound2)).lower()


def subtask8(compound1, compound2):
    """
    – obraz cesty je opět cesta
    """
    # FIXME
    return str(len(compound1) != len(compound2)).lower()


def subtask9(compound1, compound2):
    """
    – délka sledu zůstává zachována
    """
    # FIXME
    return str(len(compound1) != len(compound2)).lower()


def run(data):
    compound1 = Graph([data[0]], Component, "-")
    compound2 = Graph([data[1]], Component, "-")
    # compound1.print_graph()
    # compound2.print_graph()
    print("* |U1| = |U2|: " + str(
        subtask0(compound1, compound2)).lower())
    print("* |H1| = |H2|: " + str(
        subtask1(compound1, compound2)).lower())
    print("* Jsou-li u, v sousední uzly, pak i (u), (v) jsou sousední uzly: " +
          str(subtask2(compound1, compound2)).lower())
    print("* Grafy mají stejnou posloupnost stupňů uzlů: " +
          str(subtask3(compound1, compound2)).lower())
    print("* Pak pro každý uzel v z U platí")
    print("\t– stupeň uzlu v je roven stupni uzlu φ(v): " +
          str(subtask4(compound1, compound2)).lower())
    print("\t– množina stupňů sousedů uzlu v je rovna množině stupňů "
          "sousedů uzlu φ(v): " + str(subtask5(compound1, compound2)).lower())
    print("* Pak pro každý sled platí")
    print("\t– obraz sledu je opět sled: " + str(
          subtask6(compound1, compound2)).lower())
    print("\t– obraz tahu je opět tah: " + str(
          subtask7(compound1, compound2)).lower())
    print("\t– obraz cesty je opět cesta: " + str(
          subtask8(compound1, compound2)).lower())
    print("\t– délka sledu zůstává zachována: " +
          str(subtask9(compound1, compound2)).lower())
