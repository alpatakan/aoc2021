import re


def parse_input(input):
    lines = list()

    for l in input.splitlines():
        line = re.split(',| -> ', l)
        lines.append(dict(x1=int(line[0]), y1=int(
            line[1]), x2=int(line[2]), y2=int(line[3])))

    return lines


def create_diagram(lines):
    diagram = dict()

    for line in lines:
        if line['y1'] == line['y2']:
            start = min(line['x1'], line['x2'])
            stop = max(line['x1'], line['x2']) + 1
            for x in range(start, stop):
                key = str(x) + '.' + str(line['y1'])
                diagram[key] = 1 if key not in diagram else diagram[key] + 1
        elif line['x1'] == line['x2']:
            start = min(line['y1'], line['y2'])
            stop = max(line['y1'], line['y2']) + 1
            for y in range(start, stop):
                key = str(line['x1']) + '.' + str(y)
                diagram[key] = 1 if key not in diagram else diagram[key] + 1

    return diagram


def compute(input):
    lines = parse_input(input)
    diagram = create_diagram(lines)
    num_overlap = 0

    for key in diagram:
        if diagram[key] > 1:
            num_overlap += 1

    return num_overlap
