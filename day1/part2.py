from .part1 import parse_input


def three_measurement(input):
    numbers = list()
    for i in range(len(input) - 2):
        numbers.append(input[i] + input[i + 1] + input[i + 2])
    return numbers


def compute(input):
    result = 0
    numbers = three_measurement(parse_input(input))
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            result += 1
    return result
