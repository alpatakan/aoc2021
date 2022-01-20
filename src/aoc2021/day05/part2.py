from .part1 import parse_input


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
        else:
            xmin = min(line['x1'], line['x2'])
            xmax = max(line['x1'], line['x2'])
            ymin = min(line['y1'], line['y2'])
            ymax = max(line['y1'], line['y2'])
            xstep = 1 if line['x1'] < line['x2'] else -1
            ystep = 1 if line['y1'] < line['y2'] else -1
            for i in range(xmax - xmin + 1):
                key = str(str((xmin if xstep > 0 else xmax) + xstep * i)) + \
                    '.' + str((ymin if ystep > 0 else ymax) + ystep * i)
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
