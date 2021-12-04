def parse_input(input):
    table = list()

    for i in range(input.find('\n')):
        table.append(list())

    for l in input.splitlines():
        for i, b in enumerate(list(l)):
            table[i].append(int(b))

    return table


def compute(input):
    table = parse_input(input)
    gama, epsilon = list(), list()

    for i in range(len(table)):
        gama.append(0 if table[i].count(0) > table[i].count(1) else 1)
        epsilon.append(0 if gama[-1] == 1 else 1)

    return int(''.join(map(str, gama)), 2) * int(''.join(map(str, epsilon)), 2)
