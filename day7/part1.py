def parse_input(input):
    return list(map(lambda t: int(t), input.split(',')))


def compute(input):
    crabs = parse_input(input)
    crabs.sort()
    diff_list = []

    for i in range(max(crabs) + 1):
        diff = 0
        for j in crabs:
            diff += abs(i - j)

        diff_list.append(diff)

    return min(diff_list)
