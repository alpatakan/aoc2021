from .part1 import parse_input


def compute(input):
    nav_parsed = parse_input(input)
    score_points = {'(': 1, '[': 2, '{': 3, '<': 4}
    score_list = []

    for elem in nav_parsed:
        if elem['result'] == 'incomplete':
            total_score = 0
            elem['stack'].reverse()
            for c in elem['stack']:
                total_score *= 5
                total_score += score_points[c]
            score_list.append(total_score)

    score_list.sort()
    return score_list[int((len(score_list) - 1) / 2)]
