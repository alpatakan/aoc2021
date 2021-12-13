def parse_input(input):
    numbers = list()
    for i in input.split():
        numbers.append(int(i))
    return numbers


def compute(input):
    result = 0
    numbers = parse_input(input)
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            result += 1
    return result
