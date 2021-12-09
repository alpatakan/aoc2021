def parse_input(input):
    entries = list()
    for l in input.splitlines():
        entry = dict(outputs=[], signals=[])
        part = l.split(' | ')
        entry['signals'] = part[0].split(' ')
        entry['outputs'] = part[1].split(' ')
        entries.append(entry)

    return entries


def get_segment_map():
    a, b, c, d, e, f, g = 'a', 'b', 'c', 'd', 'e', 'f', 'g'
    segments = [None for l in range(10)]
    segments[0] = [a, b, c, e, f, g]
    segments[1] = [c, f]
    segments[2] = [a, c, d, e, g]
    segments[3] = [a, c, d, f, g]
    segments[4] = [b, c, d, f]
    segments[5] = [a, b, d, f, g]
    segments[6] = [a, b, d, e, f, g]
    segments[7] = [a, c, f]
    segments[8] = [a, b, c, d, e, f, g]
    segments[9] = [a, b, c, d, f, g]
    return segments


def get_unique_digits_list():
    return [1, 4, 7, 8]


def get_unique_match(sequence):
    segment_map = get_segment_map()

    for unique in get_unique_digits_list():
        if len(segment_map[unique]) == len(sequence):
            return segment_map[unique]

    return None


def compute(input):
    entries = parse_input(input)
    unique_total = 0

    for entry in entries:
        for output in entry['outputs']:
            if get_unique_match(output) != None:
                unique_total += 1

    return unique_total
