from .part1 import parse_input, calculate_total


def compute(input):
    return calculate_total(parse_input(input), 256)
