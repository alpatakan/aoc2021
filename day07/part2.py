from .part1 import parse_input


def compute(input):
    crabs = parse_input(input)
    crabs.sort()
    diff_list = []

    for i in range(max(crabs) + 1):
        diff = 0
        for j in crabs:
            n = abs(i - j)
            diff += int((n * (n + 1)) / 2)

        diff_list.append(diff)

    return min(diff_list)
