#!/usr/bin/env python3
from copy import deepcopy

from graphs import Graph
from nodes import Person


def name_in_polygroup(name, groups):
    for group in groups:
        if name in group and len(group) > 2:
            return True

    return False


def hax_one_member_grp(nodes, groups):
    tmp = deepcopy(groups)
    to_adjust = {}
    for grp in tmp:
        if len(grp) == 1:
            to_adjust[grp[0]] = grp

    if len(groups) == len(to_adjust):
        return groups

    adjusted_cnt = 0
    for individual in to_adjust:
        for name in sorted(nodes, reverse=True):
            if (not nodes[name].has_connection_with(individual)
                    and name_in_polygroup(name, groups)):
                to_adjust[individual].append(name)
                adjusted_cnt += 1
                break

        if adjusted_cnt == len(to_adjust):
            break

    if adjusted_cnt:
        for updated in to_adjust:
            if len(to_adjust[updated]) > 1:
                groups.remove([updated])

            to_remove = to_adjust[updated][-1]
            for group in groups:
                if to_remove in group:
                    group.remove(to_remove)

            groups.append(to_adjust[updated])

    return groups


def run(data):
    people = Graph(data, Person, " - ")
    # people.print_graph()
    groups = people.get_groups_a2()

    # hax groups
    groups = hax_one_member_grp(people.nodes, groups)

    for group in sorted(groups):
        print(", ".join(g for g in group))
