from .part1 import parse_input, get_segment_map, get_unique_match
import copy


def get_elems_other_than_these(segment_map, elems):
    not_elems = copy.deepcopy(segment_map[8])

    for elem in elems:
        if elem in not_elems:
            not_elems.remove(elem)

    return not_elems


def update_entry_map(segment_map, map, srcs, new_dsts):
    for s in srcs:
        for elem in get_elems_other_than_these(segment_map, new_dsts):
            if elem in map[s]:
                map[s].remove(elem)
                if len(map[s]) == 1:
                    map[s] = list(map[s])[0]


def remove_dsts_from_other_elems(segment_map, map, srcs, new_dsts):
    for elem in get_elems_other_than_these(segment_map, srcs):

        for new_dst in new_dsts:
            if elem not in map:
                continue
            if new_dst in map[elem]:
                map[elem].remove(new_dst)
                if len(map[elem]) == 1:
                    map[elem] = list(map[elem])[0]


def get_mapped_outputs(entry_map, outputs):
    mapped_outputs = []
    for output in outputs:
        mapped_output = []
        for elem in output:
            if elem not in entry_map:
                continue
            mapped_output.append(entry_map[elem])
        mapped_outputs.append(mapped_output)

    return mapped_outputs


def get_digit(segment_map, output):
    for i, s in enumerate(segment_map):
        if len(s) != len(output):
            continue
        if s == output:
            return i

    return None


def get_number(segment_map, outputs):
    number_str = ''
    for output in outputs:
        output.sort()
        d = get_digit(segment_map, output)
        if d == None:
            return None
        number_str += str(d)
    return int(number_str)


def do_construct_possible_maps(segment_map, possible_maps):
    completed = True
    pm_split = False
    for pm in possible_maps:
        for src in pm:
            if len(pm[src]) > 1:
                completed = False
                pm_split = True
                for dst in pm[src]:
                    new_pm = copy.deepcopy(pm)
                    update_entry_map(segment_map, new_pm, src, dst)
                    remove_dsts_from_other_elems(segment_map, new_pm, src, dst)
                    if new_pm not in possible_maps:
                        possible_maps.append(new_pm)

        if pm_split:
            possible_maps.remove(pm)
        pm_split = False

    if not completed:
        do_construct_possible_maps(segment_map, possible_maps)

    return possible_maps


def construct_possible_maps(segment_map, entry):
    possible_maps = []
    possible_maps.append(copy.deepcopy(entry['map']))
    possible_maps = do_construct_possible_maps(segment_map, possible_maps)
    return possible_maps


def compute(input):
    entries = parse_input(input)
    segment_map = get_segment_map()
    total = 0

    for entry in entries:
        entry['map'] = {segment: segment_map[8].copy()
                        for segment in segment_map[8]}

        for signal in entry['signals']:
            if get_unique_match(signal) == None or len(signal) == 7:
                continue

            update_entry_map(
                segment_map, entry['map'], signal, get_unique_match(signal))
            remove_dsts_from_other_elems(
                segment_map, entry['map'], signal, get_unique_match(signal))

        for pm in construct_possible_maps(segment_map, entry):
            n = get_number(segment_map, get_mapped_outputs(
                pm, entry['outputs']))
            if n != None:
                entry['number'] = n
                break

        total += entry['number']

    return total
