import copy
from .part1 import parse_input


def filter_table(table, pos, bit):
    iter = 0
    for i in range(len(table[pos])):
        if table[pos][iter] == bit:
            for j in range(len(table)):
                table[j].pop(iter)
            iter -= 1
        iter += 1
        if iter == len(table[pos]) or len(table[pos]) == 1:
            break

    return table


def compute(input):
    ox_table = parse_input(input)
    co_table = copy.deepcopy(ox_table)
    initial_len = len(ox_table)

    for i in range(initial_len):
        if (len(ox_table[i]) != 1):
            if ox_table[i].count(0) < ox_table[i].count(1) or ox_table[i].count(0) == ox_table[i].count(1):
                ox_discard = 0
            else:
                ox_discard = 1
            ox_table = filter_table(ox_table, i, ox_discard)

        if (len(co_table[i]) != 1):
            if co_table[i].count(0) < co_table[i].count(1) or co_table[i].count(0) == co_table[i].count(1):
                co_discard = 1
            else:
                co_discard = 0
            co_table = filter_table(co_table, i, co_discard)

    ox = list()
    co = list()
    for i in range(len(ox_table)):
        ox.append(ox_table[i][0])
    for i in range(len(co_table)):
        co.append(co_table[i][0])

    return int(''.join(map(str, ox)), 2) * int(''.join(map(str, co)), 2)
